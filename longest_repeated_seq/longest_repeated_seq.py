# https://codeclub.thorgate.eu/challenges/128

def longest_repeated_seq(word):
    l = 0 # longest seq length
    n = len(word)
    c = word[0] # char to match
    t = 0 # tmp counter

    for i in range(1,n):
        if c.lower() == word[i].lower():
            t = t+1 if t > 0 else 2 # jump to 2
        else:
            c = word[i] # set to another character
            t = 0 # reset the tmp sequence counter to zero

        if t > l:
            l = t # update the max


    return l
