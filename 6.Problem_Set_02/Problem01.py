"""
Take a number as input. Print whether it is positive , negative or Zero
"""

num = int(input("Enter a number: "))

if num > 0:
    print(f"{num} is positive")

elif num < 0:
    print(f"{num} is Negative")

else:
    print(f"Entered number({num}) is Zero")