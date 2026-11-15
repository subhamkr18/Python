def print_fibonacci(n):
    if n <= 0:
        print("Please enter a positive integer.")
        return
    
    a, b = 0, 1
    print(f"Fibonacci Series up to {n} terms:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

print_fibonacci(5)