# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

n = int(input("Enter celsius: "))
print(celsius_to_fahrenheit(n))