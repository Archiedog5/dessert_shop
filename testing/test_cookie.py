from dessert import Cookie

def test_Cookie():
    item1 = Cookie("Choclate chip", 10, 2.30)
    item2 = Cookie("Peanutbutter", 12, 5.15)
    item3 = Cookie("Mint", 1, 4.50)
    assert item1.name == "Choclate chip"
    assert item2.cookie_quantity == 12
    assert item3.price_per_dozen == 5.15
    assert item1.packaging == "Box"