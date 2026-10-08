"""
Write a Python program to take a number n from the user and print the factorial of n using a for loop.
"""

n = int(input("Enter n: "))

fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)