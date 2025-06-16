backpack = dict()
money = 100
coffee = 0
backpack['money'] = money

print("You have $" + str(money) + " in your backpack, use it wisely.\n")

print("Would you like to buy coffee for $5? (yes/no)\n")
coffee_price = 5

while True:
    coffee_question = input()
    if coffee_question == 'yes':
        money = money - coffee_price
        coffee = coffee + 1
        print("Got it! You now have $" + str(money) + "\n")
        backpack['coffee'] = coffee
        backpack['money'] = money
        break
    if coffee_question == 'no':
        print("Okay! You still have " + str(money) + "\n")
        break
    print("I'm sorry, can you repeat that?" + "\n")

print("Would you like to drink your coffee now or later? (now/later)\n")
while True:
    drink_coffee = input()
    if drink_coffee == 'now':
        coffee = coffee - 1
        backpack['coffee'] = coffee
        print("*sips coffee* you now have " + str(coffee) + " coffee(s)\n")
        print(backpack)
        break
    if drink_coffee == 'later':
        print("Okay! You still have " + str(coffee) + " coffee(s)\n")
        break
    print("I'm sorry, can you repeat that?" + "\n")

