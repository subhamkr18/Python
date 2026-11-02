n = 5

for i in range(n):
    # Print spaces
    for j in range(i):
        print(" ", end="")
        
    # Print stars
    for k in range(2 * (n - i) - 1):
        print("*", end="")
        
   
    print()