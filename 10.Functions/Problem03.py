"""
write a function called find max that takes three numbers as 
parameter and prints the largest number
"""

# 3 number , are diffent
def find_max(x,y,z):
    if x>y and x>z:
        print(f"{x} is laregest among {y} and {z}")

    elif y>x and y>z:
        print(f"{y} is laregest among {x} and {z}")

    else:
        print(f"{z} is laregest among {y} and {x}")

x=int(input("Enter 1st number: "))
y=int(input("Enter 2nd number: "))
z=int(input("Enter 3rd number: "))

find_max(x,y,z)