# https://codeclub.thorgate.eu/challenges/105

def can_i_spell_this(cards, word):
    # recursion base cases:
    if len(word) <= 0:
        return True

    word = word.upper()
    candidates = [] # final result
    letter = word[0] # currently processed letter
    for i,c in enumerate(cards):
        # one of the card letters matches the word letter
        if c[0] == letter or c[1] == letter:
            word_left = word[1:] # throw away the 'matched' letter
            cards_left = cards[:i]+cards[i+1:] # exclude the matching card
            candidates.append(can_i_spell_this(cards_left, word_left))

    return any(candidates)
