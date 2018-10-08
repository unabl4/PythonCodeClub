from person import Person, Female
from datetime import date

p = Person("Dmitri", "Sinitsa", date(1990,8,18))
assert p.full_name() == "Dmitri Sinitsa"
assert p.age() == 28

p = Female("Julia", "Kondratjeva", date(1988,3,25))
assert p.full_name() == "Julia Kondratjeva"
assert p.age() == 20    # and not 31
