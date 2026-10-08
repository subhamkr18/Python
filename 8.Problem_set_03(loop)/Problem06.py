"""
Write a Python program that takes a number n from the user and
 prints the sum of all numbers from 1 to n that are divisible by 3 using a for loop.
"""

n = int(input("Enter n: "))

sum = 0

for i in range(1, n + 1):
    if i % 3 == 0:
        sum += i

print("Sum =", sum)