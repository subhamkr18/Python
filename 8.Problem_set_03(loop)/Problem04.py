"""
Q18. Ask a number from the user, print the multiplication table upto 10.
"""

num = int(input("Enter number: "))
i=1
print(f"Multiplication table of {num} is:")
while i <=10:
    print(f"{num} X {i} = {num * i}")
    i +=1

# using for loop
'''
for i in range(1,11):
    print(f"{num} X {i} = {num * i}")
'''