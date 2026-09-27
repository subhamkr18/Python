'''
Q19. Ask a number from the user, and print all the factors.

'''

num = int(input("Enter number: "))

i = 1

print(f"factor of {num} are:")
while i <=num:
    if(num % i ==0):
        print(i, end=" ")
    i += 1