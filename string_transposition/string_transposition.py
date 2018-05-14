# https://codeclub.thorgate.eu/challenges/92

def transposition(text):
    # remove unsupported (non-alphanumeric) characters
    filtered_text = ''.join([c for c in text if c.isalnum() or c.isspace()])
    if len(filtered_text) <= 0: # filtered everything out?
        return ''
    words = filtered_text.split() # normalize spaces
    n = max(map(lambda word: len(word), words)) # get max 'length'

    lines = []
    for i in range(n): # move rows
        line = [] # current line
        for word in words:
            item = word[i] if i < len(word) else ' '
            line.append(item)
        
        # convert line to string
        # remove potential extra spaces on the right side
        string = ' '.join(line)
        lines.append(string)

    return '\n'.join(lines) + '\n'
