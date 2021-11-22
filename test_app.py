from app import change


def test_change():
    assert [{5: 'quarters'}, {1: 'nickels'}, {4: 'pennies'}] == change(1.34)
    
    
# def test_change_x_100():
#     assert [f"This is Change for 1.34 x 100",
#     {"536": "quarters"}] == change_x_100(1.34)