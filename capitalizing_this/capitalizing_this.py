# https://codeclub.thorgate.eu/challenges/111

# 'str' = 'input_string'
def capitalizing_this(str):
    cap = True # true if to do capitalization, false otherwise
    chars = list(str) # get chars

    for idx, c in enumerate(chars):
        if c == ' ': # delimiter (e.g space)?
            cap = True # reset
            continue # go to the next character

        if cap:
            cap = False
            chars[idx] = c.upper() # uppercase
        else:
            chars[idx] = c.lower()

    return ''.join(chars) # -> string