"""
Take numbers as input from the user ane by one . skip negative numbers and keep adding the positive ones. 
stop when the useruser enters 0 and print the total.(use both continue and break.)
"""

total=0
while True:
    num = int(input("Enter number: "))
    if num == 0:
        break
    elif num < 0:
        continue
    else:
        total += num

print("Total : ",total)
