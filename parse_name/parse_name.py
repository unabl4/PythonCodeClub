# https://codeclub.thorgate.eu/challenges/47
def is_name(name):
    if len(name) <= 0:
        return False

    return name[0].isupper() and name[1:].isalpha()

def is_english(char):
    o = ord(char)
    l = range(ord('a'), ord('z')+1) # lowercase chars ascii range
    u = range(ord('A'), ord('Z')+1) # uppercase chars ascii range
    return o in l or o in u

def parse_name(sentence):
    # sanitize the input, i.e remove non-english characters
    letters = lambda x: is_english(x) or x.isspace()
    words = ''.join(filter(letters, sentence)).split()
    names = list(filter(lambda xy: xy[0] > 0 and is_name(xy[1]), enumerate(words)))
    return ' '.join(map(lambda x: x[1], names))

# ---

assert is_english('a') == True
assert is_english('z') == True
assert is_english('A') == True
assert is_english('Z') == True
assert is_english('б') == False

# ---

assert is_name('') == False
assert is_name('Name') == True
assert is_name('Name1') == False
assert is_name('name') == False
assert is_name('NAME') == True

# ---

assert parse_name('') == ''
assert parse_name('One') == ''
assert parse_name('One Two three') == 'Two'
assert parse_name('I was having fun at CodeClub the other night!') == 'CodeClub'
assert parse_name('My name is Taavi') == 'Taavi'
assert parse_name(' My name is Taavi ') == 'Taavi'
assert parse_name('Hey look, is this Elon Musk over there?') == 'Elon Musk'
assert parse_name('You know, Taavi told me that you can always ask Alan if you have any questions related to Python') == 'Taavi Alan Python'
assert parse_name('Ok1 Hello2 Tere3') == 'Hello Tere'
assert parse_name('OkФ HelloГ TereШ') == 'Hello Tere'
