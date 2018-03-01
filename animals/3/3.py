# https://codeclub.thorgate.eu/challenges/45

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

class Cat(Animal):
    # class attribute override
    TYPE = 'cat'

    def __init__(self, name, friendly = True):
        self.friendly = friendly
        super().__init__(name, pet = True)

    def speak(self):
        return 'purr' if self.is_friendly() else 'meow' # ternary

    def is_friendly(self):
        return self.friendly

# ---

a = Cat("Alice")
assert a.speak() == 'purr' # friendly speak?
assert a.is_friendly() == True
assert a.is_pet() == True # always
assert str(a) == "I'm cat named Alice"

b = Cat("Bob", friendly = False)
assert b.speak() == 'meow' # friendly speak?
assert b.is_friendly() == False
assert b.is_pet() == True # always
assert str(b) == "I'm cat named Bob"
