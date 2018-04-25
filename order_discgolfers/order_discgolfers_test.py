from order_discgolfers import order_discgolfers

# tests
assert order_discgolfers([]) == [] # no score, no players, no order
assert order_discgolfers([{'a':2,'b':1}]) == ['b','a'] # lowest to highest
assert order_discgolfers([{'a':1,'b':1}]) == ['a','b'] # full tie

# challenge description example
scores = [{
    'bob': 3,
    'patric': 2,
    'squidward': 4,
}, {
    'bob': 3,
    'patric': 3,
    'squidward': 3,
}, {
    'bob': 3,
    'patric': 3,
    'squidward': 2,
}, {
    'bob': 3,
    'patric': 3,
    'squidward': 3,
}]

assert order_discgolfers(scores) == ['squidward', 'patric', 'bob']

# full draw
scores = [{'c':2,'b':2,'a':2}, {'c':2,'b':2,'a':2}]
assert order_discgolfers(scores) == ['a','b','c'] # sort alphabetically

# ?
scores = [{'c':2,'b':2,'a':2}, {'c':2,'b':2,'a':3}]
assert order_discgolfers(scores) == ['b','c','a']

# ?
scores = [{'c':2,'b':2,'a':2}, {'c':2,'b':2,'a':1}]
assert order_discgolfers(scores) == ['a','b','c']

scores = [{'c':1,'b':2,'a':3}, {'c':3,'b':3,'a':3}]
assert order_discgolfers(scores) == ['c','b','a']

# second tee is the decisive one
# should ignore the very first tee
scores = [{'a':1,'b':2},{'a':3,'b':2},{'a':2,'b':2}]
assert order_discgolfers(scores) == ['b','a']