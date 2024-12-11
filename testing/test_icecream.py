from dessert import IceCream

def test_IceCream():
    item1 = IceCream("Choclate", 2, 2.30)
    item2 = IceCream("Vinlla", 1, 1.00)
    item3 = IceCream("Choclate Mint", 1, 2.15)
    assert item1.name == "Choclate"
    assert item2.scoop_count == 1
    assert item3.price_per_scoop == 2.15
    assert item1.packaging == "Bowl"