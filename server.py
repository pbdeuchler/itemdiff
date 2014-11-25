from flask import Flask
from flask import request
from flask import jsonify

from werkzeug.exceptions import BadRequest

import diff

"""
    itemdiff
    ~~~~~~~~~~~~~~

    Simple python webserver to diff agnostic sets of "things".

    POST /diff/
    Sample Request:
    {
        sets: [
            [1, 2, 3],
            ["apple", "pear", "plum"]
        ]
    }

    :copyright: (c) 2014 Philip Deuchler.
"""

app = Flask(__name__)


class BaseException(Exception):
    status_code = 500
    message = "Server Error"

    def __init__(self, payload=None):
        self.payload = payload if payload is not None else {}


class InvalidMimeType(BaseException):
    status_code = 415
    message = "Invalid Mime Type. Please use Content-Type:application/json"


class InvalidJson(BaseException):
    status_code = 400
    message = "Invalid JSON"


class NoContent(BaseException):
    status_code = 400
    message = "There was no content to compare"


class DiffFailure(BaseException):
    status_code = 503
    message = "There was a failure with your diff"


@app.errorhandler(InvalidMimeType)
def handle_invalid_mime(error):
    return error_factory(error)


@app.errorhandler(InvalidJson)
def handle_invalid_json(error):
    return error_factory(error)


@app.errorhandler(NoContent)
def handle_no_content(error):
    return error_factory(error)


@app.errorhandler(DiffFailure)
def handle_diff_failure(error):
    return error_factory(error)


def error_factory(error):
    error_dict = dict(list(error.payload.items()) + list({'message': error.message}.items()))
    response = jsonify(error_dict)
    response.status_code = error.status_code
    return response


# Get da input
def parse_input(data):
    try:
        return [set(tmp) for tmp in data['sets']], len(data['sets'])
    except:  # forgive me python gods, but i'm too lazy to specify particular errors right now
        raise InvalidJson({'error': "Malformed content, POST data must be a dictionary containing a single key of \"sets\" with an accompanying value of a list of sets to diff"})


@app.route("/v1/diff/", methods=['POST', ])
def diff_tannen():
    request_data = None
    try:
        request_data = request.get_json(force=True)
        if request_data is None:
            pass  # is this something that happens?
    except BadRequest:
        raise InvalidJson
    # sets, n, directive = parse_input(request_data)
    sets, n = parse_input(request_data)
    result = diff.diffy_lube(sets, n)
    return jsonify(result)


if __name__ == "__main__":
    app.run()
