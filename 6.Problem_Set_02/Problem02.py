"""
Take two number as input . print the Greater of the two. if they are equal, print "Both are equal"
"""

num1= int(input("Enter 1st number: "))
num2= int(input("Enter 2nd number: "))

# checking which is greater or both are equal

if(num1 == num2):
    print("Both are Equal")

elif num1 > num2:
    print(f"{num1} is greater than {num2}")

else:
    print(f"{num2} is greater than {num1}")