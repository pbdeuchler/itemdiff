# Brings home the bacon
def diffy_lube(sets, n):
    result = {
        "disjoint": False,
        "intersection": [],
        "difference": []
        }
    intersection = sets[0].intersection(*sets[1:])
    # The below doesn't work so well, since it depends on which set is first on the list
    # Plus, we should make this general for n sized comparisons
    # mathematical_difference = sets[0].difference(*sets[1:])
    symmetric_difference = sets[0].symmetric_difference(*sets[1:])
    result["intersection"] = list(intersection)
    result["difference"] = list(symmetric_difference)
    # result["mathematical_difference"] = list(mathematical_difference)
    return result
