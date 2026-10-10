"""
Write a Python program to define a function is_prime(n) that takes an integer as an argument and checks whether it is a prime number or not. 
The function should return True if the number is prime and False otherwise. Take a number from the user and display the result.
"""
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")