'''
Write a function power(base, exp) that returns base raised to exp using a
loop - no ** operator or pow() allowed.
'''

def power(base, exp):
    if exp == 0:
        return 1

    # Handle negative exponents: base^(-n) == (1 / base)^n
    if exp < 0:
        base = 1 / base
        exp = -exp

    result = 1
    for _ in range(exp):
        result *= base

    return result

#function call
print(power(2, 5))   
print(power(3, 0))   
print(power(2, -3))  
print(power(-4, 3))   