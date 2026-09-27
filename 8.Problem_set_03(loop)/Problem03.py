"""
Q17. Sum of all the numbers from 1 to 100 divisible by 2 and 7.

"""
sum =0 
"""
for i in range(1,101):
    if(i%2==0 and i%7==0):
        sum +=i
print("Sum of all the numbers from 1 to 100 divisible by 2 and 7.",sum)
"""
#using while loop

i =1
while i <=100:
    if(i%2==0 and i%7==0):
        sum += i
    i +=1
print("Sum of all the numbers from 1 to 100 divisible by 2 and 7.",sum)
