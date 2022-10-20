from tkinter import *
from tkinter import messagebox
import funcion1 as db

bread1 = ""
toasted1 = ""
meat1 = ""
cheese1 = ""
price1 = 0.00
pricemeat = 0.00

bread2 = ""
meat2 = ""
toasted2 = ""
cheese2 = ""
price2 = 2.5
pricemeat2 = 0
veggies1 = []
saucelist1 = []
condimentlist1 = []

root = Tk()
root.geometry("800x800")
root.config(background="forest green")
def orderpage1():
	def selectbread():
		global bread1
		global price1
		global meat1
		if (breadoption.get()) == 1:
			bread1 = "White 6 inch-"
			price1 = 1.50
			monitor.config(text=bread1+(str(price1)+"$"))
		elif (breadoption.get()) == 2:
			bread1 = "White 12 inch-"
			price1 = 2.50
			monitor.config(text=bread1+(str(price1)+"$"))
		elif (breadoption.get()) == 3:
			bread1 = "Italian 6 inch-"
			price1 = 1.50
			monitor.config(text=bread1+(str(price1)+"$"))
		elif (breadoption.get()) == 4:
			bread1 = "Italian 12 inch-"
			price1 = 2.50
			monitor.config(text=bread1+(str(price1)+"$"))
		elif (breadoption.get()) == 5:
			bread1 = "Wheat 6 inch-"
			price1 = 1.50
			monitor.config(text=bread1+(str(price1)+"$"))
		elif (breadoption.get()) == 6:
			bread1 = "Wheat 12 inch-"
			price1 = 2.50
			monitor.config(text=bread1+(str(price1)+"$"))
		else:
			pass

	def selecttoasted():
		global toasted1
		if (toastedoption.get()) == 1:
			toasted1 = "toasted-"
			monitor.config(text=bread1+toasted1+(str(price1)+"$"))
		elif (toastedoption.get()) == 2:
			toasted1 = "untoasted-"
			monitor.config(text=bread1+toasted1+(str(price1)+"$"))
		else :
			pass

	def selectmeat():
		global meat1
		global pricemeat
		global price1
		if (meatoption.get()) == 1:
			meat1 = "Ham-"
			if price1 == 1.5 :
				pricemeat = 3.00
			elif price1 == 2.50 :
				pricemeat = 6.00
			monitor.config(text=bread1+toasted1+meat1+(str(price1+pricemeat)+"$"))

		elif (meatoption.get()) == 2:
			meat1 = "Turkey-"
			if price1 == 1.50 :
				pricemeat = 3.50
			elif price1 == 2.50 :
				pricemeat = 7.00
			monitor.config(text=bread1+toasted1+meat1+(str(price1+pricemeat)+"$"))
		elif (meatoption.get()) == 3:
			meat1 = "Italian-"
			if price1 == 1.50 :
				pricemeat = 3.00
			elif price1 == 2.50 :
				pricemeat = 6.00
			monitor.config(text=bread1+toasted1+meat1+(str(price1+pricemeat)+"$"))
		elif (meatoption.get()) == 4:
			meat1 = "Turkey and Ham-"
			if price1 == 1.50:
				pricemeat = 3.25
			elif price1 == 2.50:
				pricemeat = 6.50
			monitor.config(text=bread1+toasted1+meat1+(str(price1+pricemeat)+"$"))
		elif (meatoption.get()) == 5:
			meat1 = "Grilled Chicken-"
			if price1 == 1.50:
				pricemeat = 4.00
			elif price1 == 2.50:
				pricemeat = 8.00
			monitor.config(text=bread1+toasted1+meat1+(str(price1+pricemeat)+"$"))
		elif (meatoption.get()) == 6:
			meat1 = "Steak-"
			if price1 == 1.50:
				pricemeat = 4.00
			elif price1 == 2.50:
				pricemeat = 8.00
			monitor.config(text=bread1+toasted1+meat1+(str(price1+pricemeat)+"$"))

	def selectcheese():
		global meat1
		global pricemeat
		global price1
		global cheese1
		if (cheeseoption.get()) == 1:
			cheese1 = "Swiss-"
			monitor.config(text=bread1+toasted1+meat1+cheese1+(str(price1+pricemeat)+"$"))
		elif (cheeseoption.get()) == 2:
			cheese1 = "Provolone-"
			monitor.config(text=bread1+toasted1+meat1+cheese1+(str(price1+pricemeat)+"$"))
		elif (cheeseoption.get()) == 3:
			cheese1 = "Mozzarella-"
			monitor.config(text=bread1+toasted1+meat1+cheese1+(str(price1+pricemeat)+"$"))
		elif (cheeseoption.get()) == 4:
			cheese1 = "Cheddar-"
			monitor.config(text=bread1+toasted1+meat1+cheese1+(str(price1+pricemeat)+"$"))
		elif (cheeseoption.get()) == 5:
			cheese1 = "Vermont-"
			monitor.config(text=bread1+toasted1+meat1+cheese1+(str(price1+pricemeat)+"$"))
		elif (cheeseoption.get()) == 6:
			cheese1 = "Yellow-"
			monitor.config(text=bread1+toasted1+meat1+cheese1+(str(price1+pricemeat)+"$"))


	def reset():
		global bread1
		global meat1
		global toasted1
		global cheese1
		global price1
		global pricemeat
		global bread2
		global meat2
		global toasted2
		global cheese2
		global price2
		global pricemeat2
		if len(bread1) and len(meat1) and len(toasted1) and len(cheese1) > 0:
			if price1 and pricemeat != 0 :
				bread2 = bread1[:-1]
				meat2 = meat1[:-1]
				toasted2 = toasted1[:-1]
				cheese2 = cheese1[:-1]
				price2 = price1
				pricemeat2 = pricemeat
				breadoption.set(None)
				meatoption.set(None)
				toastedoption.set(None)
				cheeseoption.set(None)
				monitor.config(text="")
				bread1 = ""
				meat1 = ""
				toasted1 = ""
				cheese1 = ""
				price1 = 0
				pricemeat = 0
				print(bread1)
				print(toasted1)
				print(meat1)
				print(cheese1)
				print(price1)
				print(pricemeat)
				print(bread2)
				print(toasted2)
				print(meat2)
				print(cheese2)
				print(price2)
				print(pricemeat2)
				clear()
		
	breadoption = IntVar()
	meatoption = IntVar()
	toastedoption = IntVar()
	cheeseoption = IntVar()

	Label(text="WELCOME TO THE SELF ORDER SYSTEM",background="forest green").grid(row=0,column=1)
	Radiobutton(root, text="White 6 inch",background="forest green", variable=breadoption, value=1, command=selectbread).grid(row=1,column=0)
	Radiobutton(root, text="White 12 inch",background="forest green", variable=breadoption, value=2, command=selectbread).grid(row=1,column=1)
	Radiobutton(root, text="Italian 6 inch",background="forest green", variable=breadoption, value=3, command=selectbread).grid(row=1,column=3)
	Label(root,text="\n",background="forest green").grid(row=2,column=0)
	Radiobutton(root, text="Italian 12 inch",background="forest green", variable=breadoption, value=4, command=selectbread).grid(row=4,column=0)
	Radiobutton(root, text="Wheat 6 inch",background="forest green", variable=breadoption, value=5, command=selectbread).grid(row=4,column=1)
	Radiobutton(root, text="Wheat 12 inch",background="forest green", variable=breadoption, value=6, command=selectbread).grid(row=4,column=3)
	Label(root,text="\n",background="forest green").grid(row=5,column=0)
	Label(root,text="Please select the type of bread above",background="forest green").grid(columnspan=5,row=6,column=0)
	"""Is asking the customer to select the type of bread"""

	Radiobutton(root, text="Toasted",background="forest green", variable=toastedoption, value=1, command=selecttoasted).grid(row=7,column=0)
	Radiobutton(root, text="Untoasted",background="forest green", variable=toastedoption, value=2, command=selecttoasted).grid(row=7,column=2)
	Label(root,text="\n",background="forest green").grid(row=8,column=0)
	Label(root,text="Please select if you want to toast your sandwich!",background="forest green").grid(columnspan=5,row=9,column=0)
	"""Is asking the customer to select if he wants his sandwich toasted"""
	
	Radiobutton(root, text="Ham",background="forest green", variable=meatoption, value=1, command=selectmeat).grid(row=10,column=0)
	Radiobutton(root, text="Turkey",background="forest green", variable=meatoption, value=2, command=selectmeat).grid(row=10,column=2)
	Label(root,text="\n",background="forest green").grid(row=11,column=0)
	Radiobutton(root, text="Italian(Ham,Salami,Pepperoni)",background="forest green", variable=meatoption, value=3, command=selectmeat).grid(row=12,column=0)
	Radiobutton(root, text="Turkey and Ham",background="forest green", variable=meatoption, value=4, command=selectmeat).grid(row=12,column=2)
	Label(root,text="\n",background="forest green").grid(row=13,column=0)
	Radiobutton(root, text="Grilled Chicken",background="forest green", variable=meatoption, value=5, command=selectmeat).grid(row=14,column=0)
	Radiobutton(root, text="Steak",background="forest green", variable=meatoption, value=6, command=selectmeat).grid(row=14,column=2)
	Label(root,text="\n",background="forest green").grid(row=15,column=0)
	Label(root,text="Please select the type of meat above",background="forest green").grid(columnspan=5,row=16,column=0)
	"""Is asking the customer to select the type of meat"""

	Radiobutton(root, text="Swiss",background="forest green", variable=cheeseoption, value=1, command=selectcheese).grid(row=17,column=0)
	Radiobutton(root, text="Provolone",background="forest green", variable=cheeseoption, value=2, command=selectcheese).grid(row=18,column=2)
	Label(root,text="\n",background="forest green").grid(row=19,column=0)
	Radiobutton(root, text="Mozzarella",background="forest green", variable=cheeseoption, value=3, command=selectcheese).grid(row=20,column=0)
	Radiobutton(root, text="Cheedar",background="forest green", variable=cheeseoption, value=4, command=selectcheese).grid(row=21,column=2)
	Label(root,text="\n",background="forest green").grid(row=22,column=0)
	Radiobutton(root, text="Vermont",background="forest green", variable=cheeseoption, value=5, command=selectcheese).grid(row=23,column=0)
	Radiobutton(root, text="Yellow",background="forest green", variable=cheeseoption, value=6, command=selectcheese).grid(row=24,column=2)
	Label(root,text="\n",background="forest green").grid(row=25,column=0)
	Label(root,text="Please select the type of cheese above",background="forest green").grid(columnspan=5,row=25,column=0)
	"""Is asking the customer to select the type of cheese"""




	monitor = Label(root,background="forest green")
	monitor.grid(columnspan=3,row=27,column=0)

	Button(root, text="Next Page", command=reset,background="forest green").grid(row=28,column=1)

	def clear():
		list = root.grid_slaves()
		for l in list:
			l.destroy()
		orderpage2()

def orderpage2():
	global bread2
	global meat2
	global toasted2
	global cheese2
	global price2
	global pricemeat2

	def clear():
		list = root.grid_slaves()
		for l in list:
			l.destroy()
		orderpage1()

	

	tomato = IntVar()
	lettuce = IntVar()
	onion = IntVar()
	pickles = IntVar()
	hotpeppers = IntVar()
	olives = IntVar()
	mayo = IntVar()
	caesar = IntVar()
	ranch = IntVar()
	russian = IntVar()
	buffalo = IntVar()
	ketchup = IntVar()
	salt = IntVar()
	pepper = IntVar()
	oregano = IntVar()
	crpepper = IntVar()

	def selectveggies():
		veg = ""
		veglist= []
		global veggies1
		if (tomato.get()) == 1:
			veg+="-With tomatoes"
			if price2 == 1.50:
				veglist.append("2-Tomatoes")
			elif price2 == 2.50:
				veglist.append("4-Tomatoes")
		else :
			pass
		if (lettuce.get()) == 1:
			veg+="-With lettuce"
			if price2 == 1.50:
				veglist.append("1 ounce of lettuce")
			elif price2 == 2.50:
				veglist.append("2 ounces of lettuce")
		else :
			pass
		if (onion.get()) == 1:
			veg+="-With onions"
			if price2 == 1.50:
				veglist.append("1 scoop of onions")
			elif price2 == 2.50:
				veglist.append("2 scoops of onions")
		else :
			pass
		if (pickles.get()) == 1:
			veg+="-With pickle chips"
			if price2 == 1.50:
				veglist.append("4 pickle chips")
			elif price2 == 2.50:
				veglist.append("8 pickle chips")
		else :
			pass
		if (hotpeppers.get()) == 1:
			veg+="-With hot peppers"
			if price2 == 1.50:
				veglist.append("1 scoop of hot peppers")
			elif price2 == 2.50:
				veglist.append("2 scoop of hot peppers")
		else :
			pass
		if (olives.get()) == 1:
			veg+="-With black olives"
			if price2 == 1.50:
				veglist.append("1 scoop of black olives")
			elif price2 == 2.50:
				veglist.append("2 scoops of black olives")
		else :
			pass
		veggies1 = veglist
		monitorveg.config(text=veg)

	def selectsauces():
		sauce = ""
		saucelist= []
		global saucelist1
		if (mayo.get()) == 1:
			sauce+="-With mayonnaise"
			if price2 == 1.50:
				saucelist.append("1 ounce of mayo")
			elif price2 == 2.50:
				saucelist.append("2 ounces of mayo")
		else :
			pass
		if (caesar.get()) == 1:
			sauce+="-With caesar"
			if price2 == 1.50:
				saucelist.append("1 ounce of caesar")
			elif price2 == 2.50:
				saucelist.append("2 ounces of caesar")
		else:
			pass
		if (ranch.get()) == 1:
			sauce+="-With ranch"
			if price2 == 1.50:
				saucelist.append("1 ounce of ranch")
			elif price2 == 2.50:
				saucelist.append("2 ounces of ranch")
		else :
			pass
		if (russian.get()) == 1:
			sauce+="-With russian"
			if price2 == 1.50:
				saucelist.append("1 ounce of russian")
			elif price2 == 2.50:
				saucelist.append("2 ounces of russian")
		else :
			pass
		if (buffalo.get()) == 1:
			sauce+="-With buffalo"
			if price2 == 1.50:
				saucelist.append("1 ounce of buffalo")
			elif price2 == 2.50:
				saucelist.append("2 ounces of buffalo")
		else :
			pass
		if (ketchup.get()) == 1:
			sauce+="-With ketchup"
			if price2 == 1.50:
				saucelist.append("1 ounce of ketchup")
			elif price2 == 2.50:
				saucelist.append("2 ounces of ketchup")
		else :
			pass
		saucelist1 = saucelist
		monitorsauce.config(text=sauce)

	def selectcondiments():
		condiments = ""
		condimentlist= []
		global condimentlist1
		if (salt.get()) == 1:
			condiments+="-With salt"
			if price2 == 1.50:
				condimentlist.append("3 shakes of salt")
			elif price2 == 2.50:
				condimentlist.append("6 shakes of salt")
		else :
			pass
		if (pepper.get()) == 1:
			condiments+="-With pepper"
			if price2 == 1.50:
				condimentlist.append("3 shakes of pepper")
			elif price2 == 2.50:
				condimentlist.append("6 shakes of pepper")
		else:
			pass
		if (oregano.get()) == 1:
			condiments+="-With oregano"
			if price2 == 1.50:
				condimentlist.append("3 shakes of oregano")
			elif price2 == 2.50:
				condimentlist.append("6 shakes of oregano")
		else :
			pass
		if (crpepper.get()) == 1:
			condiments+="-With crushed red pepper"
			if price2 == 1.50:
				condimentlist.append("3 shakes of crushed red pepper")
			elif price2 == 2.50:
				condimentlist.append("6 shakes of crushed red pepper")
		else :
			pass
		condimentlist1 = condimentlist
		monitorcondiment.config(text=condiments)

	def submitorder():
		submit()
		retrieve()
		clear()
	
	Label(root,text="PLEASE SELECT YOUR TOPPINGS!",background="forest green").grid(row=0,column=3)
	Label(root,text="\n",background="forest green").grid(row=1,column=0)
	Checkbutton(root,text="Tomato",background="forest green",variable=tomato,onvalue=1,offvalue=0,command=selectveggies).grid(row=2,columnspan=2,column=0)
	Checkbutton(root,text="Lettuce",background="forest green",variable=lettuce,onvalue=1,offvalue=0,command=selectveggies).grid(row=2,columnspan=2,column=2)
	Checkbutton(root,text="Onion",background="forest green",variable=onion,onvalue=1,offvalue=0,command=selectveggies).grid(row=2,columnspan=3,column=4)
	Label(root,text="\n",background="forest green").grid(row=3,column=0)
	Checkbutton(root,text="Pickle chips",background="forest green",variable=pickles,onvalue=1,offvalue=0,command=selectveggies).grid(row=5,columnspan=2,column=0)
	Checkbutton(root,text="Hot peppers",background="forest green",variable=hotpeppers,onvalue=1,offvalue=0,command=selectveggies).grid(row=5,columnspan=2,column=2)
	Checkbutton(root,text="Black olives",background="forest green",variable=olives,onvalue=1,offvalue=0,command=selectveggies).grid(row=5,columnspan=2,column=4)
	Label(root,text="\n",background="forest green").grid(row=6,column=0)
	Label(root,text="Please select the vegetables you want to add!",background="forest green").grid(columnspan=7,row=7,column=0)
	"""Is asking the vegetables"""

	Label(root,text="\n",background="forest green").grid(row=8,column=0)
	Checkbutton(root,text="Mayonnaise",background="forest green",variable=mayo,onvalue=1,offvalue=0,command=selectsauces).grid(row=9,columnspan=2,column=0)
	Checkbutton(root,text="Caesar",background="forest green",variable=caesar,onvalue=1,offvalue=0,command=selectsauces).grid(row=9,columnspan=2,column=2)
	Checkbutton(root,text="Ranch",background="forest green",variable=ranch,onvalue=1,offvalue=0,command=selectsauces).grid(row=9,columnspan=3,column=4)
	Label(root,text="\n",background="forest green").grid(row=10,column=0)
	Checkbutton(root,text="Russian",background="forest green",variable=russian,onvalue=1,offvalue=0,command=selectsauces).grid(row=11,columnspan=2,column=0)
	Checkbutton(root,text="Buffalo",background="forest green",variable=buffalo,onvalue=1,offvalue=0,command=selectsauces).grid(row=11,columnspan=2,column=2)
	Checkbutton(root,text="Ketchup",background="forest green",variable=ketchup,onvalue=1,offvalue=0,command=selectsauces).grid(row=11,columnspan=2,column=4)
	Label(root,text="\n",background="forest green").grid(row=12,column=0)
	Label(root,text="Please select the sauces you want to add!",background="forest green").grid(columnspan=7,row=13,column=0)
	"""Is asking the vegetables"""
	
	Label(root,text="\n",background="forest green").grid(row=14,column=0)
	Checkbutton(root,text="Salt",background="forest green",variable=salt,onvalue=1,offvalue=0,command=selectcondiments).grid(row=15,column=2)
	Checkbutton(root,text="Pepper",background="forest green",variable=pepper,onvalue=1,offvalue=0,command=selectcondiments).grid(row=15,column=4)
	Label(root,text="\n",background="forest green").grid(row=16,column=0)
	Checkbutton(root,text="Oregano",background="forest green",variable=oregano,onvalue=1,offvalue=0,command=selectcondiments).grid(row=17,column=2)
	Checkbutton(root,text="Crushed Red Pepper",background="forest green",variable=crpepper,onvalue=1,offvalue=0,command=selectcondiments).grid(row=17,column=4)	
	Label(root,text="\n",background="forest green").grid(row=18,column=0)
	Label(root,text="Please select the Condiments you want to add!",background="forest green").grid(columnspan=7,row=19,column=0)
	"""Is asking the vegetables"""

	monitorveg = Label(root,background="forest green")
	monitorveg.grid(columnspan=20,row=20,column=0)
	monitorsauce = Label(root,background="forest green")
	monitorsauce.grid(columnspan=20,row=21,column=0)
	monitorcondiment = Label(root,background="forest green")
	monitorcondiment.grid(columnspan=20,row=22,column=0)

	Button(text="Submit order",command=submitorder,background="forest green").grid(row=23)
	Button(text="Cancel order",command=clear).grid(row=23,column=2)
	#TODO

def submit():
    global id_count
    id_count = 1 if id_count >= 100 else int(id_count) + 1
    bread = bread2
    toasted = toasted2
    meat = meat2
    cheese = cheese2
    veggies = veggies1
    sauces = saucelist1
    condiments = condimentlist1
    paid = False
    id = id_count
    showed = False
    price = (price2+pricemeat2)

    db.Orders.create_order(bread,toasted,meat,cheese,veggies,sauces,condiments,paid,id,showed,price)
    messagebox.showinfo('Order created','Your order number is {}\nThank you for placing your order!'.format(id))



def retrieve():
	showed = False
	order_retrieved = db.Orders.retrieve_order(showed)
	print(order_retrieved) if order_retrieved else None

id_count = 0

orderpage1()

root.mainloop()