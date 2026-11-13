# Program to print numbers divisible by both 3 and 5 between 51 and 109

print("Numbers divisible by 3 and 5 between 51 and 109:")
for num in range(51, 110):  
    if num % 3 == 0 and num % 5 == 0:
        print(num)