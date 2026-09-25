"""
Take a number as input. Print the result of that number raised to the
power of 3 using **. Also print what // 7 and % 7 give for the same number.
"""

num = int(input("Enter number: "))

# Printing power of 3
print(f"{num} of power 3 is: {num ** 3}")

#Printing floor division and remainder with 7

print(f"Floor division of {num} with 7 is: {num // 7} \n Remainder of {num} with 7 is: {num % 7}")