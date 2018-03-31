from can_i_spell_this import can_i_spell_this

# tests

# base cases
assert can_i_spell_this((), '') == True
assert can_i_spell_this((), 'A') == False
assert can_i_spell_this((('A','B'),), '') == True

assert can_i_spell_this((('A','B'), ('C','D')), 'AB') == False
assert can_i_spell_this((('A','B'), ('A','C')), 'A') == True
assert can_i_spell_this((('A','B'),), 'a') == True
assert can_i_spell_this((('A','B'),), 'AB') == False
assert can_i_spell_this((('A','B'), ('E','B')), 'AB') == True
#
assert can_i_spell_this((('A','B'),('A','E'),('B','C')), 'ABA') == True
assert can_i_spell_this((('A','B'),('A','E'),('B','C')), 'ABa') == True

# reverse order of cards and letters
assert can_i_spell_this((('V','G'),('A','B'),('V','W')), 'VAG') == True

# duplicate letters
assert can_i_spell_this((('S','Z'),('A','C')), 'CSS') == False # 'S' needs to have two cards
