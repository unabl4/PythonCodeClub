from snek_detector import is_it_python

assert is_it_python("print('Hoooly moly')") == True
assert is_it_python("This is a valid sentence indeed, but not a valid Python sentence.") == False
