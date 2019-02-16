# https://pyspace.eu/ws/thorgate/ch/38/
from unittest import mock # new

def meaning_of_life_universe_and_everything(modifier):
    """
    returns 42 + modifier
    """
    raise NotImplementedError('idk')

class LifeAdvice:
    # Wrap in staticmethod because we do not want to pass `self` to the external function
    happiness_func = staticmethod(meaning_of_life_universe_and_everything)

    def personal_modifier(self, birth_month, birth_day):
        """Returns the Lucky Life Number of a person based on their birthday"""
        return int((birth_day * birth_month) % 6.66)

    def how_to_be_happy(self):
        # The life advice currently only works for people with a birthday on April 20th
        mod = self.personal_modifier(4, 20)
        magic_number = self.happiness_func(mod)
        return f'Invest in stocks that have the number {magic_number} in them'

# ---

def test_happiness():
    # mock to return 42 constantly
    with mock.patch.object(LifeAdvice, 'happiness_func', return_value=42) as mocked_happiness_func:
        life_advice = LifeAdvice()
        ret_val = life_advice.how_to_be_happy() # -> string

        # note that no exception was raised
        mocked_happiness_func.assert_called()
        mocked_happiness_func.assert_called_once_with(0)

        assert ret_val == 'Invest in stocks that have the number 42 in them'
