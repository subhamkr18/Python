#Write a Python program using a function to find all the factors of a given number.
def find_factors(n):
    factors = []

    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)

    return factors


num = int(input("Enter a number: "))

print("Factors of", num, "are:", find_factors(num))