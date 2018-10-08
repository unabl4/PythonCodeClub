from datetime import date
class Person:
    def __init__(self, first_name, last_name, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    def age(self):
        return int((date.today()-self.birth_date).days // 365.25)

    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)
