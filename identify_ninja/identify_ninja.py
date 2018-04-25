# https://codeclub.thorgate.eu/challenges/115

# checks if two given words are anagrams of one another
def is_anagram(word1, word2):
    # lengths must be the same
    if len(word1) != len(word2):
        return False

    chars = list(word2)

    for c in list(word1):
        found = False 

        # inner loop
        for idx, char in enumerate(chars):
            if c == char:
                found = True # mark as found
                chars[idx] = None # checkout
                break

        if found: # character found ->
            continue # move on to the next one
        else:
            return False # char not found

    return True # everything checks out
    
# main func
def identify_ninja(ninja_name, villagers):
    m = filter(lambda villager: is_anagram(ninja_name, villager), villagers)
    return list(m)