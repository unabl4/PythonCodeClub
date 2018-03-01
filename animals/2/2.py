# https://codeclub.thorgate.eu/challenges/43

# inheritance
class SilentError(NotImplementedError):
    pass

class Animal:
    # class attribute
    TYPE = 'unknown'

    # constructor
    def __init__(self, name, pet = False):
        self.name = name
        self.pet = pet

    # ---

    def speak(self):
        raise SilentError # cannot speak still

    def is_pet(self):
        return self.pet

    def __str__(self):
        return "I'm {} named {}".format(self.TYPE, self.name)

# ---

a = Animal("Joe")
try:
    a.speak()
except SilentError:
    pass # correct
else:
    raise AssertionError('Exception expected')

assert a.is_pet() == False
assert str(a) == "I'm unknown named Joe"

b = Animal("Bill", pet = True)
try:
    b.speak()
except SilentError:
    pass # correct
else:
    raise AssertionError('Exception expected')
assert b.is_pet() == True
assert str(b) == "I'm unknown named Bill"

c = Animal("Alice", pet = False)
try:
    c.speak()
except SilentError:
    pass # correct
else:
    raise AssertionError('Exception expected')
assert c.is_pet() == False # explicit
assert str(c) == "I'm unknown named Alice"
