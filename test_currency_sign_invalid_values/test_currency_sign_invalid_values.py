# https://pyspace.eu/ws/thorgate/ch/37/
import pytest

def currency_sign_from_name(name):
    mapping = {
        'euro': '€',
        'dollar': '$',
        'pound': '£'
    }

    if name.lower() in mapping:
        return mapping[name.lower()]
    raise ValueError(f'Name of currency not one of ["euro", "dollar", "pound"]')

# ---

@pytest.mark.parametrize('name', ['foo','bar','baz']) # definitely not currencies
def test_currency_sign_invalid_values(name):
    with pytest.raises(ValueError) as exception:
        currency_sign_from_name(name)

    assert str(exception.value) == f'Name of currency not one of ["euro", "dollar", "pound"]'
