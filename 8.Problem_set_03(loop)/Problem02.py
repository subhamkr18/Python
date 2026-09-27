"""
Sum of all the numbers from 1 to 100.

"""
sum =0

# using for loop
'''
for i in range(1,101):
    sum +=i
print("Sum of all no from 1 to 100 : ",sum)
'''

# using while loop
i=1
while i <= 100:
    sum += i
    i += 1
print("Sum of all no from 1 to 100 : ",sum)