menu = {
    "pizza": 300,
    "burger": 40,
    "pasta": 100,
    "coffee": 20,
    "momos": 50
}


order_list = []
total_bill = 0


print("Welcome to our restraunt. Here is the menu - \npizza - RS.300 \nburger - RS.40 \npasta - RS.100 \ncoffee - RS.20 \nmomos - Rs.50" )

while True:
    order = input("Enter your item you want to order = ".lower())
    if order in menu:
        quantity = int(input("enter your quantity"))
        item_cost = menu[order]*quantity
        total_bill += item_cost
        order_list.append((order, quantity, item_cost))
        print(quantity,order,"had been added","subtotal: RS.",item_cost)
    else:
        print("this item is not available ")

    choice = input("do you want to order anything else? YES/NO")
    if choice.upper() == "NO":
        print("\nThank you! Your order is being prepared.")
        break

print("final order",order_list)
print("total bill :",total_bill)

    



