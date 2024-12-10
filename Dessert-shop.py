from receipt import make_receipt
from dessert import(
    DesserItems,
    Candy,
    Cookie,
    IceCream,
    Sundae,


) 



class Order:
    def __init__(self):
        self.Order_list=[]
        self.total=0

    def add(self, DesserItems):
        # print(DesserItems)
        self.Order_list.append(DesserItems)

    def reper(self):
        item_amount=0
        for item in self.Order_list:
            print(item)
            item_amount+=1
        print("There is",(item_amount), "items in your order list.")
        return item_amount
    
    def order_cost(self):
        for item in self.Order_list:
            self.total+=item.calculate_cost()
        return self.total
    
    def order_tax(self):
        tax=self.total.calculate_tax()
        return tax
    
    def __str__(self):
        string = ""
        for value in self.order:
            string += value.name + "\n"

        return string
    
class DessertShop:

    def __init__(self):
        pass

    def user_prompt_candy(self):
        try:
            stored = Candy("", 0, 0)
            stored.name=input('What is the name of the candy?: ')
            stored.candy_weight=float(input("How many pounds do you want?: "))
            stored.price_per_pound=float(input("Whats the price per pound?: "))
            return stored
        except:
            print("We don't have that.")
    def user_prompt_cookie(self):
        try:
            stored = Cookie("", 0, 0)
            stored.name=input('What is the name of the cookie?: ')
            stored.cookie_quantity=int(input("How many cookies do you want?: "))
            stored.price_per_dozen=float(input("Whats the price per a dozen?: "))
            return stored
        except:
            print("We don't have that.")

    def user_prompt_icecream(self):
        try:
            stored = IceCream("", 0, 0)
            stored.name=input('What is the name of the ice cream flavor?: ')
            stored.scoop_count=int(input("How many scoops do you want?: "))
            stored.price_per_scoop=float(input("Whats the price per a scoop?: "))
            return stored
        except:
            print("We don't have that.")

    def user_prompt_sundae(self):
        try:
            stored = Sundae("", 0, 0, "", 0)
            stored.name=input('What is the name of the ice cream flavor?: ')
            stored.scoop_count=int(input("How many scoops do you want?: "))
            stored.price_per_scoop=float(input("Whats the price per a scoop?: "))
            stored.topping_name=input('What topping do you want?: ')
            stored.topping_price=float(input('Whats the cost of that topping?: '))
            return stored
        except:
            print("We don't have that.")
    

    

def main():
    shop = DessertShop() 
    order = Order()
    lst=[['Name',"Cost",'Tax']]
    # order.add(['Name',"cost",'tax'])
    sub_total=0
    tax_total=0
    x=order.reper()
    # print(Candy('Candy Corn', 1.5, 0.25))
    # order.add(Candy('Candy Corn', 1.5, 0.25))
    # order.add(Candy('Gummy Bears', 0.25, 0.35))
    # order.add(Cookie('Chocolate Chip', 6, 3.99))
    # order.add(IceCream('Pistachio', 2, 0.79))
    # order.add(Sundae('Vanilla', 3, 0.69, 'Hot Fudge', 1.29))
    # order.add(Cookie('Oatmeal Raisin', 2, 3.45))

    # boolean done = false
    done: bool = False
    # build the prompt string once
    prompt = '\n'.join([ '\n',
            '1: Candy',
            '2: Cookie',            
            '3: Ice Cream',
            '4: Sunday',
            '\nWhat would you like to add to the order? (1-4, Enter for done): '
      ])

    while not done:
      choice = input(prompt)
      match choice:
        case '':
          done = True
        case '1':            
          item = shop.user_prompt_candy()
          order.add(item)
          print(f'{item.name} has been added to your order.')
        case '2':            
          item = shop.user_prompt_cookie()
          order.add(item)
          print(f'{item.name} has been added to your order.')
        case '3':            
          item = shop.user_prompt_icecream()
          order.add(item)
          print(f'{item.name} has been added to your order.')
        case '4':            
          item = shop.user_prompt_sundae()
          order.add(item)
          print(f'{item.topping_name} {item.name} sundae has been added to your order.')
        case _:            
          print('Invalid response:  Please enter a choice from the menu (1-4) or Enter')

    print(order.Order_list)
    for item in order.Order_list:
        # print("RAN")
# 
        print(f"This is the item: {item}")
        # print(f"This is the Order_list: {order.Order_list}")
    
        # order.Order_list.append([item.name, round(item.calculate_cost(),2), round(item.calculate_tax(),2)])
        lst.append([item.name, item.calculate_cost(), item.calculate_tax()])
        sub_total+=round(item.calculate_cost(),2)
        tax_total+=item.calculate_tax()

    gimmy=round(tax_total,2)
    grand_total=sub_total+tax_total
    timmy=round(grand_total,2)
    x=order.reper()
    order.add(['Order Subtotals', sub_total, gimmy])
    order.add(['Order Total',timmy,''])
    order.add(['Total items in the order','',x])

    print("List: ", lst)
    
    make_receipt(lst, "receipt")

main()