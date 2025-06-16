import time
from classes.player import PClasses


print("Hello adventurer! Please enter your name:")
playername = input()
print("\nWelcome " + playername + ", to the land of Zoshary!")
time.sleep(1)

warrior = PClasses("Warrior", 200)
wizard = PClasses("Wizard", 140)
archer = PClasses("Archer", 180)

print("Please choose a class (1/2/3):")
print("1. Warrior\n2. Wizard\n3. Archer")
playerclass = int(input())

