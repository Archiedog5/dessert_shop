from dessert import Sundae

def test_Sundae():
    item1 = Sundae("Choclate", 2, 2.30, 'sprinkels', 0.15)
    item2 = Sundae("Vinlla", 1, 1.00, 'choclate sause', 0.35)
    item3 = Sundae("Choclate Mint", 1, 2.15, 'wip cream', 0.45)
    assert item1.name == "Choclate"
    assert item2.scoop_count == 1
    assert item3.price_per_scoop == 2.15
    assert item3.topping_name == 'wip cream'
    assert item2.topping_price == 0.35
    assert item1.packaging == "Boat"