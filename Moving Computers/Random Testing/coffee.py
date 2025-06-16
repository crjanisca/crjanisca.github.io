print("\nHello welcome to Cru's Coffee!!!")
name = input("What is your name?\n")
print("\nHello " + name + ", thank you so much for coming in today!\n\n\n")

menu = ["Americano", "Espresso", "Cappucino", "Latte", "Mocha", "Frappucino"]
print(name + ", what would you like to order today? This is what we have on our menu:\n" + ', '.join(menu) + "\n")

order = input()
if order == "Americano":
    price = 4
elif order == "Espresso":
    price = 6
elif order == "Cappucino":
    price = 5
elif order == "Latte":
    price = 5
elif order == "Mocha":
    price = 6
elif order == "Frappucino":
    price = 8
    
while True:
    if order in menu:
        print("\nGotcha, how many would would you like to buy?\n")
        quantity = input()
        break
    else:
        print("\nI'm sorry, that isn't on our menu. Here's our menu if you need to see it again:\n" + ', '.join(menu) + "\n")
        order = input()

print("\nOkay! Would you like a cookie with your order for $5? (Yes/No)\n")
cookie = input()

if cookie == "Yes":
    total = price * int(quantity) + 5
elif cookie == "No":
    total = price * int(quantity)
    
#if cookie != "Yes" or cookie != "No":
#    print("I'm sorry, I didn't understand what you said... Can you say that again?")

if quantity > str(1):
    print("\nOkay! Your total is: $" + str(total) + ". We'll have your " + quantity + " " + order + "s ready in just a moment!")
else:
    print("\nOkay! Your total is: $" + str(total) + ". We'll have your " + order + " ready in just a moment!")
