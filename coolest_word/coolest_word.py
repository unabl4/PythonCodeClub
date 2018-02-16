# https://codeclub.thorgate.eu/challenges/102
# finds the 'coolest' word
def coolest_word(words):
    if len(words) <= 0:
        return None

    # mapping
    m = map(lambda w: (w, len(set(w))), words)
    c = max(m, key=lambda x: x[1]) # max by the value
    return c[0] # return the word itself

# ---

assert coolest_word([]) == None
assert coolest_word(['ok', 'oo']) == 'ok'
assert coolest_word(['expectation', 'discomfort', 'half', 'decomposition']) == 'decomposition'
assert coolest_word(['abc', 'def']) in ['abc', 'def'] # either of them
assert coolest_word(['ab', 'cdef']) == 'cdef'
assert coolest_word(['Aa', 'bb']) == 'Aa'
