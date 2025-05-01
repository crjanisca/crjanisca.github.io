
unit = input("Is the temperature in C or F?: ")
temp = int(input("Enter a temperature: "))

if unit == "C":
    temp = temp * 1.8 + 32
    unit = "F"
    print(f"Your temperature is {round(temp, 1)}{unit}°")
elif unit == "F":
    temp = 0.556 * (temp - 32)
    unit = "C"
    print(f"Your temperature is {round(temp, 1)}{unit}°")
else:
    print(f"{unit} is not valid")