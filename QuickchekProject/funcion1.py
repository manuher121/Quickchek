import csv

class Sandwich:
    def __init__(self,bread,toasted,meat,cheese,veggies,sauces,condiments,paid,id,showed,price):
        self.bread = bread
        self.toasted = toasted
        self.meat = meat
        self.cheese = cheese
        self.veggies = veggies
        self.sauces = sauces
        self.condiments = condiments
        self.paid = paid
        self.id = id
        self.showed = showed
        self.price = price

    def __str__(self):
        return f"{self.bread}\n{self.toasted}\n{self.meat}\n{self.cheese}\n{self.veggies}\n{self.sauces}\n{self.condiments}\n{self.paid}\n{self.id}\n{self.showed}\n{self.price}"

class Orders:
    orders = []
    with open("orders.csv", newline='\n') as file:
        reader = csv.reader(file, delimiter=';')
        for bread, toasted, meat, cheese, veggies, sauces, condiments, paid, id, showed, price in reader:
            order = Sandwich(bread, toasted, meat, cheese, veggies, sauces, condiments, paid, id, showed, price)
            orders.append(order)

    orders2 = []

    @staticmethod
    def retrieve_order(showed):
        for i,order in enumerate(Orders.orders):
            if order.showed == showed:
                Orders.orders[i].showed = True
                return order

    @staticmethod
    def create_order(bread, toasted, meat, cheese, veggies, sauces, condiments, paid, id, showed, price):
        order = Sandwich(bread, toasted, meat, cheese, veggies, sauces, condiments, paid, id, showed, price)
        Orders.orders.append(order)
        Orders.savefile()
        return order

    @staticmethod
    def pay_order(id,paid):
        for order in Orders.orders:
            if order.id == id and paid == False:
                return order

    @staticmethod
    def showed_status(showed):
        pass

    @staticmethod
    def erase_order_1(showed):
        for i,order in enumerate(Orders.orders):
            if order.showed == showed:
                return Orders.orders.pop(i)

    @staticmethod
    def savefile():
        with open("orders.csv",'w',newline='\n') as file:
            writer = csv.writer(file, delimiter=";")
            for order in Orders.orders:
                writer.writerow((order.bread, order.toasted, order.meat, order.cheese, order.veggies,
                                    order.sauces, order.condiments, order.paid, order.id, order.showed,
                                    order.price))
                return order