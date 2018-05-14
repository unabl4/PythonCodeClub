# https://codeclub.thorgate.eu/challenges/79

def product(iterable):
    p = 1
    for n in iterable:
        p *= n
    return p

def max_product_of_quintet(numbers):
    assert len(numbers) >= 5 # exception otherwise

    numbers.sort()

    # numbers selection
    candidates = []
    for i in range(6):
        right = [] if i == 5 else numbers[-5+i:]
        num_set = numbers[:i]+right # take most positive and most negative numbers
        candidates.append(product(num_set))
    
    return max(candidates)