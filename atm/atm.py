from typing import Dict

class ATM:
    MIN_BILL_TOTAL_VAL = 5000 # default
    # supported list of bills (names) and their values
    BILLS = {
        'fives': 5,
        'tens': 10,
        'twenties': 20,
        'fifties': 50,
        'hundreds': 100,
        'thundreds': 200,
        'fhundreds': 500
    }

    # ---

    # constructor
    def __init__(self, **kwargs: Dict[str, int]):
        self.bills = {}

        # set default value(s)
        for bill in self.BILLS:
            bill_value = self.BILLS[bill] # nominal
            self.bills[bill_value] = self.MIN_BILL_TOTAL_VAL // bill_value

        # override bills
        if kwargs:
            for bill in kwargs:
                value = kwargs[bill]

                # reset
                if not isinstance(value, int) or value < 0:
                    value = 0

                # bill is supported?
                # ignore otherwise
                bill_value = self.BILLS.get(bill)
                if bill_value:
                    self.bills[bill_value] = value

    # ---

    def bills_left(self):
        return self.bills

    # return the balance
    def money_left(self):
        return sum(map(lambda b: b[0] * b[1], self.bills.items()))

    # int input is guaranteed
    def withdraw(self, amount: int):
        if amount <= 0 or amount > self.money_left():
            return 0

        withdrawal = self._withdraw(amount, {})
        if withdrawal:
            # update the bills left
            for bill in withdrawal:
                self.bills[bill] -= withdrawal[bill]
            return withdrawal
        else:
            return 0

    def deposit(self, new_bills: Dict[int, int]):
        # check if dictionary
        if not isinstance(new_bills, dict):
            return # do nothing

        # available bill values
        bill_values = self.BILLS.values() # 5,10,20, etc ...

        for k,v in new_bills.items():
            # counterfeit bill?
            if k not in bill_values:
                continue # skip

            # check the count value
            if not isinstance(v, int) or v <= 0:
                continue # ignore

            # update
            self.bills[k] += v

    # ---

    def _withdraw(self, amount: int, bills: Dict[int, int]):
        # base case(s)
        if amount == 0:
            return bills
        elif amount < 5: # (-inf..5) -> not possible; 5 - smallest bill
            return {}

        # hereafter, amount >= 5

        # return available bills, 'excluding' the selected ones
        free_bills = { k:v-bills.get(k,0) for k,v in self.bills.items() if v-bills.get(k,0) > 0 }

        # select the greatest possible bill strictly smaller than the amount (priority); 
        # one tier lower
        bill_lower = max(filter(lambda bill: bill < amount, free_bills), default=None)

        if bill_lower: # found the bill (at least one)
            count = min(amount // bill_lower, free_bills[bill_lower]) # number of bills (possible)
            new_amount = amount - (count * bill_lower) # residual
            bills.setdefault(bill_lower, 0) # required, do not remove
            bills[bill_lower] += count # update the selected bills dict
            return self._withdraw(new_amount, bills) # recursion with a smaller sub-problem
        else:
            # exact amount
            if free_bills[amount]: # > 0
                bills.setdefault(amount,0) # required, do not remove
                bills[amount] += 1
                return bills # new amount = 0
            else:
                return {} # not possible