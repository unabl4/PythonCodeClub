from string_transposition import transposition

text = 'Hello, World!'
trsp = """H W
e o
l r
l l
o d
"""
assert transposition(text) == trsp

text = 'Python CodeClub @ Tallinn'
trsp = """P C T
y o a
t d l
h e l
o C i
n l n
  u n
  b  
"""
assert transposition(text) == trsp

# ---

text = 'AB CDEF G'
trsp = """A C G
B D  
  E  
  F  
"""
assert transposition(text) == trsp