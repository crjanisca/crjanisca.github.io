# Import
import math
import time

# Variables
strings = "Example"
integers = 18
floats = 3.14
booleans = True

print(f"{floats} is an {strings} of a float")

# Typecasting
booleans = str(booleans)
floats = int(floats)
integers = float(integers)
strings  = bool(strings)

# Input
name = input("What is your name?: ")
print(f"Hello {name}!")
age = int(input("How old are you?: "))
age_soon = age + 1
print(f"You'll be {age_soon} soon!")

# Standard Arithmetic Operators
computers = 0
computers = computers + 2 #addition
computers = computers - 2 #subtraction
computers = computers * 2 #multiplication
computers = computers / 2 #division
computers = computers ** 2 #to the power of _
computers = computers % 2 #modulous (gives remainder of equation)

# Augmented Arithmetic Operators
computers += 2
computers -= 2
computers *= 2
computers /= 2
computers **= 2
computers %= 2

# Math Functions
print(math.pi) #print pi
print(math.e) #print e 

x = 3.14
y = 4
z = 5

round = round(x)
absolute = abs(y)
power = pow(4, 3)

print(round)
print(absolute)
print(power)

square_root = math.sqrt(y)
round_up = math.ceil(x)
round_down = math.floor(x)

print(square_root)
print(round_up)
print(round_down)

radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius #circumferene of a circle

radius = float(input("Enter the radius of a circle: "))
area = math.pi * pow(radius, 2) #area of a circle

print(circumference)
print(area)

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a, 2) + pow(b,2))

print(f"Side C = {c}")

# If/Else Statements
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible for a credit card")
elif age < 0:
    print("You have not been born yet")
elif age > 100:
    print("You are not eligible for a credit card (must be 18-100)")
elif age == "":
    print("You have not entered an age")
else:
    print("You are not eligible for a credit card (must be 18+)")

# Logical Operators
temp = 25
is_raining = False
is_sunny = True

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still on")

if temp >= 28 and is_sunny:
    print("It's HOT outside")
    print("It's SUNNY")
elif temp <= 0 and is_sunny:
    print("It's FREEZING")
    print("It's SUNNY")
elif temp >= 28 and not is_sunny:
    print("It's HOT")
    print("It's CLOUDY")
elif temp >= 0 and not is_sunny:
    print("It's FREEZING")
    print("It's CLOUDY")

# Conditional Expressions
num = 5
h = 10
j = 12
age = 18

polarity = "Positive" if num > 0 else "Negative"
result = "EVEN" if num % 2 == 0 else "ODD"
greater = h if h > j else j
status = "Adult" if age >= 18 else "Child"

# String Methods
name = input("Full Name: ")

result = len(name)
first = name.find("x") #find first occurance of character
last = name.rfind("y") #find last occurance of character
capitalize = name.capitalize() #capitalizes first letter in string
upper = name.upper() #makes all letters capital
lower = name.lower() #makes all letters lowercase
isdigit = name.isdigit() #checks if characters are all digits
isalpha = name.isalpha() #checks if characters are all alphabetical
count = name.count("l") #counts how many of specified character are in string
replace = name.replace("to_replace", "replacement") #replaces character(s) with other specified character(s)

print(help(str)) #prints a guide on strings

# String Indexing
credit_number = "1234-5678-9012-3456"

print(credit_number[0 : 4]) #prints the first 4 characters of the string [start : end : step]
print(credit_number[0 :]) #prints full string
print(credit_number[-4 :]) #prints the last 4 characters of the string
print(credit_number[::2]) #prints every other character in string starting at the first character
print(credit_number[::-1]) #reverses the string

last_digits = credit_number[-4 :]
print(f"XXXX-XXXX-XXXX-{last_digits}")

# Format Specifiers
price1 = 3.14159

print(f"Price 1 is {price1:.10f}") #how many digits go after decimal point
print(f"Price 1 is {price1:10}") #how many digits go before decimal point
print(f"Price 1 is {price1:010}") #turns blank digits into zeros
print(f"Price 1 is {price1:<10f}") #left justify
print(f"Price 1 is {price1:>10f}") #right justify
print(f"Price 1 is {price1:^10f}") #centered
print(f"Price 1 is {price1:+}") #adds + before positive numbers
print(f"Price 1 is {price1: }") #lines up positive numbers without + evenly with negative numbers
print(f"Price 1 is {price1:,}") #adds comma every 1000th place (eg. 1,234,456)
print(f"Price 1 is {price1:+,.10f}") #formatting can be combined

# While Loops
name = input("Enter your name: ")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ") #after requirement is met the while loop is exited and script continues
    
print(f"Hello {name}")


age = int(input("Enter your age: "))

while age < 0:
    print("Age cannot be negative")
    age = int(input("Enter your age: "))

print(f"You are {age} years old")


food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter a food you like (q to quit): ")

print("Goodbye")

# For Loops
for x in reversed(range(1, 11)):
    print(x)
    time.sleep(1) #import time (will wait 1s)
print("HAPPY NEW YEAR!")

for x in range(1,21):
    if x == 13:
        continue #skips the number 13
    else:
        print(x)

# Nested Loops
for x in range(3): #will loop the nested loop 3 times
    for y in range(1,10):
        print(y, end="")
    print() #prints a new line after each loop

# Lists, Sets, Tuples
fruits = ["apple", "orange", "banana", "coconut", "pineapple"] #ordered, changeable, duplicates allowed
for fruit in fruits:
    print(fruit)

fruits.append("kiwi") #adds to the end of the list
fruits.insert(0, "grape") #adds to the specified position in the list
fruits.remove("banana") #removes the first occurance of the specified item
fruits.pop(0) #removes the item at the specified position in the list
fruits.sort() #sorts the list in alphabetical order
fruits.reverse() #reverses the order of the list
fruits.clear() #clears the list of all items
fruits.count("apple") #counts how many of the specified item are in the list

print(fruits.index("apple")) #returns the index of the specified item
print(len(fruits)) #prints the length of the list
print(dir(fruits)) #prints all the functions that can be used with lists
print(help(fruits)) #prints a guide on lists

vegetables = {"carrot", "broccoli", "spinach", "potato", "cabbage"} #unordered, unchangeable but can add/remove, duplicates NOT allowed

print(vegetables.index("broccoli")) #returns the index of the specified item
print(len(vegetables)) #prints the length of the set
print(dir(vegetables)) #prints all the functions that can be used with sets
print(help(vegetables)) #prints a guide on sets

vegetables.add("onion") #adds to the specified position in the set
vegetables.remove("carrot") #removes the specified item
vegetables.pop() #removes the first item in the set (which is random))
vegetables.clear() #clears the set of all items

instruments = ("guitar", "piano", "drums", "bass", "saxophone") #ordered, unchangeable, duplicates allowed

print(instruments.index("guitar")) #returns the index of the specified item
print(len(instruments)) #prints the length of the tuple
print(dir(instruments)) #prints all the functions that can be used with tuples
print(help(instruments)) #prints a guide on tuples

instruments.count("guitar") #counts how many of the specified item are in the tuple

# 2D Lists
fruits =     ["apple", "orange", "banana", "coconut", "pineapple"]
vegetables = ["carrot", "broccoli", "spinach", "potato", "cabbage"]
meats =      ["chicken", "beef", "pork", "fish", "lamb"]

groceries = [fruits, vegetables, meats] #creates a 2D list
other_groceries = [ ["apple", "orange", "banana", "coconut", "pineapple"], 
                    ["carrot", "broccoli", "spinach", "potato", "cabbage"], 
                    ["chicken", "beef", "pork", "fish", "lamb"]] #also creates a 2D list

print(groceries[0]) #prints the row listed
print(groceries[0][0]) #prints the specified item in the table

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print() #prints a new line after each loop

# Dictionaries

captials = {"USA": "Washington D.C.",
            "Pakistan": "Islamabad",
            "Nepal": "Kathmandu",
            "Sri Lanka": "Colombo"}

print(dir(captials)) #prints all the functions that can be used with dictionaries
print(help(captials)) #prints a guide on dictionaries
print(captials.get("Japan")) #returns None if the specified item is not in the dictionary
