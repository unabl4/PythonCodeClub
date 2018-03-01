# https://codeclub.thorgate.eu/challenges/2

# swaps the first and last characters of a string 's'
def charswap(s):
    # strings are immutable -> convert to list first
    t = list(str(s))
    if not t: # empty list cannot be used to access elements
        return ''
    t[0], t[-1] = t[-1], t[0] # swap
    return ''.join(t) # list -> string


assert charswap('') == ''
assert charswap('a') == 'a'
assert charswap('Taavi') == 'iaavT'
assert charswap(1234) == '4231' # int
assert charswap('Hello World') == 'dello WorlH'
