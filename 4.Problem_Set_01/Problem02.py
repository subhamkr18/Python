"""
Take a number as input. Print whether it is even or odd using the %
operator and a comparison operator.
"""

num = int(input("Enter Number: "))

# Checking whether number is even or odd
if(num % 2 == 0):
    print(f"{num} is Even")
else:
    print(f"{num } id Odd")