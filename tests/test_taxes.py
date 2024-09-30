import pytest
from src.taxes import calculate_taxes

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