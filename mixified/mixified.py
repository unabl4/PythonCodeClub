# https://codeclub.thorgate.eu/challenges/6
# checks if a given word is mixified or not
def is_mixified(word):
    n = len(word) # length
    if n <= 2:
        return False

    c = None # next character lowercase expectation
    for i in range(0,n):
        # special character / digit?
        if not word[i].isalpha():
            c = None # reset
            continue # go to the next character

        if c == None:
            # assumed to be correct
            c = word[i].isupper()
        else:
            if c != word[i].islower():
                return False

            # update the lowercase expectation for the next character
            c = not c

    return True

# returns the number of mixified words
def count_mixified(paragraph):
    words = paragraph.split() # ?
    return list(map(is_mixified, words)).count(True)

# ---

# assertions (tests)
assert is_mixified('') == False, 'Blank string is NOT mixified (len is less than 2)'
assert is_mixified('T') == False, 'Single character string is NOT mixified'
assert is_mixified('Tt') == False
assert is_mixified('tT') == False
assert is_mixified('TT') == False
assert is_mixified('1') == False, 'Single digit is NOT mixified'
assert is_mixified('AbCd') == True, 'AbCd IS mixified'
assert is_mixified('aBcD') == True, 'aBcD is mixified' # ?
assert is_mixified('ABCD') == False, 'ABCD is NOT mixified'

assert is_mixified('GoOd-hEaRtEd') == True, 'Challenge example is mixified'
assert is_mixified('GoOd-hEaRtEd.') == True, 'Challenge example is mixified'
assert is_mixified('GoOd--hEaRtEd') == True # ?
assert is_mixified('GoOd-HeArTeD') == True
assert is_mixified('GoOd-HeArTed') == False

assert count_mixified('') == 0
assert count_mixified('He Wo') == 0
assert count_mixified('HeLlO WoRlD') == 2
assert count_mixified('HeLLo WoRlD') == 1
assert count_mixified('Hello World') == 0
assert count_mixified('GoOd-hEaRtEd.') == 1
assert count_mixified(' GoOd-hEaRtEd. ') == 1
assert count_mixified(' GoOd--hEaRtEd') == 1
