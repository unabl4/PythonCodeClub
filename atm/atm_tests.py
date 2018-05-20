from atm import ATM

# ---
# atm instantiation

# default atm
atm = ATM() 
assert atm.money_left() == 35000
assert atm.bills_left() == { 5: 1000, 10: 500, 20: 250, 50: 100, 100: 50, 200: 25, 500: 10 }

# override correctly
atm = ATM(fhundreds=15)
assert atm.money_left() == 37500
assert atm.bills_left() == { 5: 1000, 10: 500, 20: 250, 50: 100, 100: 50, 200: 25, 500: 15 }

# incorrect bill value(s)
atm = ATM(fives=-10) # negative value
assert atm.money_left() == 30000
assert atm.bills_left() == { 5: 0, 10: 500, 20: 250, 50: 100, 100: 50, 200: 25, 500: 10 } 

atm = ATM(fives='s') # str not int
assert atm.money_left() == 30000
assert atm.bills_left() == { 5: 0, 10: 500, 20: 250, 50: 100, 100: 50, 200: 25, 500: 10 }

atm = ATM(fives=10.0) # float instead of int -> ?
assert atm.money_left() == 30000
assert atm.bills_left() == { 5: 0, 10: 500, 20: 250, 50: 100, 100: 50, 200: 25, 500: 10 }

# ---
# atm deposit

# counterfeit
atm = ATM()
atm.deposit({40: 10}) # 40 is an invalid bill
assert atm.money_left() == 35000
assert atm.bills_left() == { 5: 1000, 10: 500, 20: 250, 50: 100, 100: 50, 200: 25, 500: 10 }

atm = ATM()
atm.deposit({10: -10}) # negative value
assert atm.money_left() == 35000
assert atm.bills_left() == { 5: 1000, 10: 500, 20: 250, 50: 100, 100: 50, 200: 25, 500: 10 }

atm = ATM()
atm.deposit({5: 10}) # +50
assert atm.money_left() == 35050 # +50
assert atm.bills_left() == { 5: 1010, 10: 500, 20: 250, 50: 100, 100: 50, 200: 25, 500: 10 }


# ---
# withdrawal

atm = ATM()
assert atm.withdraw(71) == 0 # not possible (1<5)
assert atm.money_left() == 35000
assert atm.bills_left() == { 5: 1000, 10: 500, 20: 250, 50: 100, 100: 50, 200: 25, 500: 10 }

atm = ATM()
assert atm.withdraw(-10) == 0 # not possible (negative amount)
assert atm.money_left() == 35000
assert atm.bills_left() == { 5: 1000, 10: 500, 20: 250, 50: 100, 100: 50, 200: 25, 500: 10 }

atm = ATM()
assert atm.withdraw(100) == { 50: 2 }
assert atm.money_left() == 34900
assert atm.bills_left() == { 5: 1000, 10: 500, 20: 250, 50: 98, 100: 50, 200: 25, 500: 10 }

atm = ATM()
assert atm.withdraw(750) == { 500: 1, 200: 1, 20: 2, 5: 2 }
assert atm.money_left() == 34250
assert atm.bills_left() == { 5: 998, 10: 500, 20: 248, 50: 100, 100: 50, 200: 24, 500: 9 }

# special cases
# not possible to give with one bill tier lower, however exact bill is available
atm = ATM(fives=0, tens=0, twenties=1, fifties=0, hundreds=0, thundreds=0, fhundreds=0)
assert atm.withdraw(20) == { 20: 1 } # ?
assert atm.money_left() == 0
assert atm.bills_left() == { 5: 0, 10: 0, 20: 0, 50: 0, 100: 0, 200: 0, 500: 0 }

# one tier lower possible
atm = ATM(fives=0, tens=2, twenties=1, fifties=0, hundreds=0, thundreds=0, fhundreds=0)
assert atm.withdraw(20) == { 10: 2 } # ?
assert atm.money_left() == 20
assert atm.bills_left() == { 5: 0, 10: 0, 20: 1, 50: 0, 100: 0, 200: 0, 500: 0 }

atm = ATM(fives=4, tens=1, twenties=1, fifties=0, hundreds=0, thundreds=0, fhundreds=0)
assert atm.withdraw(20) == { 10: 1, 5: 2 } # ?
assert atm.money_left() == 30 # 50-20
assert atm.bills_left() == { 5: 2, 10: 0, 20: 1, 50: 0, 100: 0, 200: 0, 500: 0 }

# ---

atm = ATM(fives=0, tens=0, twenties=0, fifties=0, hundreds=0, thundreds=0, fhundreds=2)
assert atm.withdraw(1500) == 0 # not possible (1500 > 1000)
assert atm.money_left() == 1000
assert atm.bills_left() == { 5: 0, 10: 0, 20: 0, 50: 0, 100: 0, 200: 0, 500: 2 }

atm = ATM(fives=0, tens=0, twenties=0, fifties=5, hundreds=4, thundreds=0, fhundreds=2)
assert atm.withdraw(1500) == { 500: 2, 100: 4, 50: 2 }
assert atm.money_left() == 150 # 1650-1500
assert atm.bills_left() == { 5: 0, 10: 0, 20: 0, 50: 3, 100: 0, 200: 0, 500: 0 }