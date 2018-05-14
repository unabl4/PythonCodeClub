# https://codeclub.thorgate.eu/challenges/79
# alternative, **incorrect** version

def max_product_of_quintet(numbers):
    n = len(numbers)
    assert n >= 5 # exception otherwise

    p = t = numbers[0]*numbers[1]*numbers[2]*numbers[3]*numbers[4] # initial product
    i = 1
    while True:
        e = i+4 # end index
        if e >= n:
            break
        t //= numbers[i-1] # remove the previous 'number'
        t *= numbers[e]
        if t > p:
            p = t

        i += 1 # move right
    return p