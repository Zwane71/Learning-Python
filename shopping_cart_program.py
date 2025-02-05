#Exercise 2 Shopping cart program

item = str(input("What iteme would you like to buy: "))
price = float(input("What is the price: "))
quantity = int(input("How many would you like: "))

total = price * quantity
 
print(f"You have bought {quantity} x {item}") 
print(f"Your total is ${total}")