"""
Write a Python program using a function factorial(n) that takes a number as an argument
 and returns its factorial. Take a number from the user and display the result.
"""
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

num = int(input("Enter a number: "))
print("Factorial =", factorial(num))