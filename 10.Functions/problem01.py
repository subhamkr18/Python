"""
Write a function that ask a no from user and prints if that number is odd or even
"""

def check_odd_even():
    num=int(input("Enter a number: "))
    if num%2==0:
        print(f"{num} is even")

    else:
        print(f"{num} is odd")

check_odd_even()