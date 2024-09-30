import pytest
from src.taxes import calculate_taxes, calculate_tax


@pytest.fixture
def prices():
    return [100, 200, 300]

@pytest.mark.parametrize("tax_rate, expect", [(10, [110, 220, 330]),
                                              (15, [115, 230, 345]),
                                              (20, [120, 240, 360])])
def test_calculate_taxes(prices, tax_rate, expect):
    assert calculate_taxes(prices, tax_rate) == expect


def test_calculate_taxes_invalid_text_read(prices):
    with pytest.raises(ValueError):
        calculate_taxes(prices, tax_rate=-1)

def test_calculate_taxes_invalid_prices():
    with pytest.raises(ValueError):
        calculate_taxes([0, -1, -2], tax_rate=10)


@pytest.mark.parametrize('price, tax_rate, expected', [(100, 10, 110),
                                                       (50, 5, 52.5)])
def test_calculate_tax(price, tax_rate, expected):
    assert calculate_tax(price, tax_rate) == expected

def test_calculate_tax_invalid_price():
    with pytest.raises(ValueError):
        calculate_tax(-1, 10)

def test_calculate_tax_invalid_tax_price_below_zero():
    with pytest.raises(ValueError):
        calculate_tax(100, -1)

def test_calculate_tax_invalid_tax_price_after_100():
    with pytest.raises(ValueError):
        calculate_tax(100, 1000)



