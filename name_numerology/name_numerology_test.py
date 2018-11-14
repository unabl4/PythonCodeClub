from name_numerology import name_numerology

assert name_numerology(False) == 0
assert name_numerology(True) == 0
assert name_numerology(5) == 0
assert name_numerology('A') == 1
assert name_numerology('B') == 2
assert name_numerology('AI') == 10
assert name_numerology('AJ') == 2 # 11 > 10 => 1+1=2
assert name_numerology('IIIIIIIIIII') == 9
