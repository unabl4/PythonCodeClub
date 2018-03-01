# https://codeclub.thorgate.eu/challenges/43

class Animal:
    # class attribute
    TYPE = 'unknown'

    # constructor
    def __init__(self, name, pet = False):
        self.name = name
        self.pet = pet

    # ---

    def speak(self):
        return 'i cannot'

    def is_pet(self):
        return self.pet

    def __str__(self):
        return "I'm {} named {}".format(self.TYPE, self.name)

# ---

a = Animal("Joe")
assert a.speak() == 'i cannot'
assert a.is_pet() == False
assert str(a) == "I'm unknown named Joe"

b = Animal("Bill", pet = True)
assert b.speak() == 'i cannot'
assert b.is_pet() == True
assert str(b) == "I'm unknown named Bill"

c = Animal("Alice", pet = False)
assert c.speak() == 'i cannot'
assert c.is_pet() == False # explicit
assert str(c) == "I'm unknown named Alice"
