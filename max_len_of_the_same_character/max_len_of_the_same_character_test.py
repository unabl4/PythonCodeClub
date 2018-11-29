from max_len_of_the_same_character import longest_repeated_seq

assert longest_repeated_seq('hopplaaaa') == 4
assert longest_repeated_seq('hzzzZZlcccc') == 5
assert longest_repeated_seq('hzdlc5') == 0
assert longest_repeated_seq('ffBbbbaaa') == 4
assert longest_repeated_seq('abcdef') == 0
assert longest_repeated_seq('aa') == 2
assert longest_repeated_seq('aA') == 2
assert longest_repeated_seq('Aa') == 2
assert longest_repeated_seq('aaA') == 3
assert longest_repeated_seq('a') == 0
assert longest_repeated_seq('A') == 0
