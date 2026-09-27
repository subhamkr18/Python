"""
Print all the numbers which are divisible by 3 and 5, from 1 to 100
"""
print("Numbers (1-100) which are divisible by 3 and 5 are:")
for i in range (1 ,100):
    if(i%3==0 and i%5==0):
        print(i,end=" ")
