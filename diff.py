# Brings home the bacon
def diffy_lube(sets, n):
    result = {
        "disjoint": False,
        "intersection": [],
        "difference": []
        }
    result["intersection"] = list(sets[0].intersection(*sets[1:]))
    result["difference"] = list(sets[0].difference(*sets[1:]))
    return result
