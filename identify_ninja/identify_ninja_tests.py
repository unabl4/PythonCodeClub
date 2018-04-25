# https://codeclub.thorgate.eu/challenges/115

from identify_ninja import *

# tests
assert is_anagram('abc', 'cba') == True
assert is_anagram('abc', 'abd') == False
assert is_anagram('obb', 'bob') == True

assert identify_ninja('obb', ['bob', 'richard']) == ['bob']