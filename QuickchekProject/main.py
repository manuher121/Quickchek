import os
import funcion1 as db

id_count = 0

def start():
    while True:

        print("Welcome please make your order")

        option = input("=> ")
        
        if option == "1":
            for order in db.Orders.orders:
                print(order)      

        elif option == "2":
            global id_count
            id_count = 1 if id_count >= 100 else int(id_count) + 1
            bread = input("Bread ").upper()
            toasted = input("Yes or no ").upper()
            meat = input("Meat ").upper()
            cheese = input("Cheese ").upper()
            veggies = input("Veggies ").upper()
            sauces = input("Sauces ").upper()
            condiments = input("Condiments ").upper()
            paid = False
            id = id_count
            showed = False
            price = "120"
            db.Orders.create_order(bread,toasted,meat,cheese,veggies,sauces,condiments,paid,id,showed,price)
            print("Order Created!")
        elif option == "3":
            showed = False
            order_retrieved = db.Orders.retrieve_order(showed)
            print(order_retrieved) if order_retrieved else None

        elif option == "5":
            id = int(input("id number"))
            paid = False
            pay_order = db.Orders.pay_order(id,paid)
            pay_order.paid = True if pay_order else None
            print(pay_order.bread,pay_order.meat,"SUB = $",pay_order.price) if pay_order else None


        else:
            break
    #TODO