from sort_csv import sort_file

raised = False
try:
    sort_file('abc', 'test')   # -> TypeError
except TypeError:
    raised = True

assert raised, "The expected exception was not raised"

# ---

# unsupported param
raised = False
try:
    sort_file('abc', x='a')
except TypeError:
    raised = True

assert raised, "The expected exception was not raised"

# ---

# A string with only one item per row
assert sort_file('b\ny\na') == 'a\nb\ny'

# Providing some keyword arguments
assert sort_file('b,b\ny,y\na,a', outsep=':', outend='\t') == 'a:a\tb:b\ty:y'

# Blank lines and lines starting with '#' should not appear in the result
assert sort_file('b,q\n\n#p,y\na,o', outsep='-') == 'a-o\nb-q'

# Proper sorting and ignore blank lines at the end
assert sort_file('2,3,d\n2,4,x\n2,4,a\n\n\n', outend=' -- end\n') == '2,3,d -- end\n2,4,a -- end\n2,4,x'

assert sort_file('') == ''

# 2,3,d
# 1,4,d
# 8,2,z
# 2,4,x
# 2,4,a

# =>

# 1,4,d
# 2,3,d
# 2,4,a
# 2,4,x
# 8,2,z

assert sort_file('2,3,d\n1,4,d\n8,2,z\n2,4,x\n2,4,a') == '1,4,d\n2,3,d\n2,4,a\n2,4,x\n8,2,z'

assert sort_file('#\n#\n#\n') == ''

assert sort_file('\n\n\n') == ''

# wrong input separator
assert sort_file('a|\nb|\n', insep='>') == 'a|\nb|'

# first printable char
assert sort_file('a\n\t#') == 'a'
