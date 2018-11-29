def longest_repeated_seq(word):
    # not possible
    if len(word) < 2:
        return 0

    w = word.lower() # normalize
    t = w[0] # target char
    repeat = 1
    max_repeat = 0
    for c in w[1:]:
        if c == t:
            repeat += 1
            max_repeat = max(repeat, max_repeat)
        else:
            t = c # update the target
            repeat = 1 # reset
            continue

    return max_repeat
