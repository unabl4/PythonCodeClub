# https://codeclub.thorgate.eu/challenges/128

from longest_repeated_seq import *

assert longest_repeated_seq('hopplaaaa') == 4
assert longest_repeated_seq('hzzzZZlcccc') == 5
assert longest_repeated_seq('hzdlc5') == 0
assert longest_repeated_seq('ffBbbbaaa') == 4

assert longest_repeated_seq('abcdef') == 0
assert longest_repeated_seq('aaaaaa') == 6
assert longest_repeated_seq('abcdefXx') == 2
