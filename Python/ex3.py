name = input("Full Name: ")

result = len(name)
first = name.find("x") #find first occurance of character
last = name.rfind("y") #find last occurance of character
name = name.capitalize() #capitalizes first letter in string

print(name)