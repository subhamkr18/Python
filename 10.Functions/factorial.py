def calculate_factorial(n):
    """Returns the factorial of a non-negative integer n."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


number = int(input("Enter a number: "))
print(f"The factorial of {number} is {calculate_factorial(number)}")