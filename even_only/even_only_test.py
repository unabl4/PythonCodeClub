from even_only import even_only

assert even_only() == 0
assert even_only(1) == 0
assert even_only(1,2) == 2
assert even_only(2,4,6) == 12
assert even_only(1,2,3,1,1,2,4,5,6,11,123123) == 14
