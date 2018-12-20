# https://pyspace.eu/ws/thorgate/ch/36/
import pytest

def currency_sign_from_name(name):
    mapping = {
        'euro': '€',
        'dollar': '$',
        'pound': '£'
    }

    if name.lower() in mapping:
        return mapping[name.lower()]
    raise ValueError(f'Name of currency not one of {set(mapping.keys())}')

# ---

@pytest.mark.parametrize('name,sign', [('euro', '€'),('dollar', '$'),('pound', '£'),])
def test_currency_sign_valid_values(name, sign):
    assert currency_sign_from_name(name) == sign
