from abc import ABC, abstractmethod 



class DesserItems(ABC):
    def __init__(self,name):
        self.name = name
        self.tax_precent=7.25
    def __str__(self):
        return f"{self.name}"
    
    @abstractmethod
    def calculate_cost(self):
        pass

    
    def calculate_tax(self):
        tax=self.calculate_cost()*self.tax_precent*0.01
        x=round(tax,2)
        return x

class Candy(DesserItems):

    def __init__(self, name, candy_weight, price_per_pound):
        super().__init__(name)
        self.candy_weight=candy_weight
        self.price_per_pound=price_per_pound
        self.packaging="Bag"

    def calculate_cost(self):
        cost = self.candy_weight*self.price_per_pound
        x=round(cost,2)
        return x
    
    def __str__(self):
        return f"{self.name}, {self.candy_weight}lbs, ${self.price_per_pound}/lbs, {self.calculate_cost()}, {self.calculate_tax()}, {self.packaging}"
    
class Cookie(DesserItems):

    def __init__(self, name, cookie_quantity, price_per_dozen):
        super().__init__(name)
        self.cookie_quantity=cookie_quantity
        self.price_per_dozen=price_per_dozen
        self.packaging='Box'
    
    def calculate_cost(self):
        cookie_dozen = self.cookie_quantity/12
        cost = cookie_dozen*self.price_per_dozen
        x=round(cost,2)
        return x
    
    def __str__(self):
        return f"{self.name}, {self.cookie_quantity}cookies, ${self.price_per_dozen} per dozen, {self.calculate_cost()}, {self.calculate_tax()}, {self.packaging}"

class IceCream(DesserItems):
    def __init__(self, name, scoop_count, price_per_scoop):
        super().__init__(name)
        self.scoop_count=scoop_count
        self.price_per_scoop=price_per_scoop
        self.packaging='Bowl'

    def calculate_cost(self):
        cost = self.scoop_count*self.price_per_scoop
        x=round(cost,2)
        return x
    
    def __str__(self):
        return f"{self.name}, {self.scoop_count} scoops, ${self.price_per_scoop} per scoop, {self.calculate_cost()}, {self.calculate_tax()}, {self.packaging}"

class Sundae(IceCream):
    def __init__(self, name, scoop_count, price_per_scoop, topping_name, topping_price):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name=topping_name
        self.topping_price=topping_price
        self.packaging='Boat'

    def calculate_cost(self):
        cost = self.scoop_count*self.price_per_scoop
        add_on= cost+self.topping_price
        x=round(add_on,2)
        return x
    
    def __str__(self):
        return f"{self.name}, {self.scoop_count} scoops, ${self.price_per_scoop} per scoop, {self.topping_name}, {self.topping_price}, {self.calculate_cost()}, {self.calculate_tax()}, {self.packaging}"
    