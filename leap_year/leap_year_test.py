from leap_year import is_leap_year

assert is_leap_year(1600) == True
assert is_leap_year(2000) == True
assert is_leap_year(1700) == False
assert is_leap_year(1800) == False
assert is_leap_year(1900) == False
assert is_leap_year(1992) == True
assert is_leap_year(2012) == True
