from roman import roman

assert roman(1) == 'I'
assert roman(4) == 'IV' # and not 'IIII'
assert roman(5) == 'V'
assert roman(9) == 'IX'
assert roman(10) == 'X' # and not VV
