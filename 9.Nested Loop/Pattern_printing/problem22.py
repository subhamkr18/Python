def print_z_pattern(n):
    for i in range(n):
        for j in range(n):
            # Print '*' for the top row, bottom row, and the secondary diagonal
            if i == 0 or i == n - 1 or j == n - 1 - i:
                print("*", end="")
            else:
                print(" ", end="")
        print() # Move to the next line after each row

# Example usage with size 6
n = 6
print_z_pattern(n)