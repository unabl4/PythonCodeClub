def name_numerology(name):
    # special case (non-string) -> zero?
    if not isinstance(name,str):
        return 0

    s = 0 # sum
    for char in name.upper(): # normalize the casing
        c = ord(char) # char code
        if c < 65 or c > 90:
            continue # ignore the character outside the alphabet

        s += (c-65) % 9 + 1 # c-ord('A')+1

    while s > 10: # two-digit number?
        s = sum(int(i) for i in str(s))

    return s
