from person import Person
from datetime import date

p = Person("Dmitri", "Sinitsa", date(1990,8,18))
assert p.full_name() == "Dmitri Sinitsa"
assert p.age() == 28
