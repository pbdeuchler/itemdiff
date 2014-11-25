itemdiff
========

Agnostic diff sets of items (disjoint, intersection, difference)

Run
----
```bash
$ python server.py
```
- Runs on port `5000`

Use
----

- Python
```python
import requests, json
sets = {"sets": [[1, 2, 3], [1, 4, 5]]}
data_string = json.dumps(sets)
r = requests.post("http://127.0.0.1:5000/v1/diff/", data=data_string)
print(r.json())
# {u'disjoint': False, u'intersection': [1], u'difference': [2, 3]}
```

- curl
```bash
$ curl -H "Content-Type: application/json" -d '{"sets": [[1, 2, 3], [1, 4, 5]]}' http://127.0.0.1:5000/v1/diff/
```

- JSON
```json
{
  "sets": [
    [1, 2, 3], 
    [1, 4, 5]
  ]
}
```


Note
----
The returned `difference` is not a (mathematical) set difference operation, but an XOR on the sets (symmetric difference)

Todo
----
- [ ] Allow for "reference" set in request
	- allows mathematical difference
	- could allow for some cool text diff stuff
- [ ] Figure out how to identify sets while comparing

