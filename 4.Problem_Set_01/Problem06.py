"""
Take two numbers as input. Without using *
, calculate and print their product
using += in a way that adds the first number to itself the
second number of times. (Think carefully.)
"""

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

result=0

for i in range(num2):
    result += num1

print("Product is : " ,result )