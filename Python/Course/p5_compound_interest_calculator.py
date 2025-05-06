# Compound Interest Calculator

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle can't be less than or equal to zero")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Interest rate can't be less than or equal to zero")
    else:
        break

while True:
    time = float(input("Enter the time in years: "))
    if time <= 0:
        print("Time can't be less than or equal to zero")
    else:
        break

total = principle * pow((1 + rate / 100), time)
overall_interest = total - principle

print(f"Your total amount after {time} year/s will be ${total:.2f} and the overall interest earned will be ${overall_interest:.2f}")