# https://codeclub.thorgate.eu/challenges/86

# return the lowest of the two number
def lower_than(number_1, number_2):
    if number_1 == number_2:
        return 'EQUAL'
    elif number_1 < number_2:
        return number_1
    else:
        return number_2


assert lower_than(1,1) == 'EQUAL'
assert lower_than(0,1) == 0
assert lower_than(2,1) == 1
