def dictToString(dictionary):
    l = [] # list
    # dictionaries are unordered
    for key in dictionary:
        if dictionary[key] is None:
            continue # skip the key-value pair if the value is None
        l.append(key+'='+str(dictionary[key]) + ';')

    return ''.join(l) # list -> string

assert dictToString({}) == ''
assert dictToString({'test': 1, 'test2': 2}) == 'test=1;test2=2;'
assert dictToString({'test': 1, 'test2': None, 'test3': 3}) == 'test=1;test3=3;'
assert dictToString({'test': None, 'test2': None}) == ''
