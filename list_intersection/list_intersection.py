# https://codeclub.thorgate.eu/challenges/30

# finds common elements in two lists
def list_intersection(list_one, list_two):
    h = {} # dictionary storage
    common = []

    for elem in list_one:
        h[elem] = True

    for elem in list_two:
        if elem in h:
            common.append(elem)

    return common

assert list_intersection([1,3,5,7,9], [3,4,5,6,7]) == [3,5,7]
assert list_intersection([1,2,3], [4,5,6]) == []
