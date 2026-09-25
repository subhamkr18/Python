"""
Take three numbers as input. Print the largest of the three without using any
built-in function
"""
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

# checking largest among three 

if(num1 == num2 and num1 == num3):
    print("All three numbers are equal")

elif(num1 >= num2 and num1 >= num3):
    print(f"{num1} is largest among {num2} and {num3}")

elif(num2 >= num1 and num2 >= num3):
    print(f"{num2} is largest among {num1} and {num3}")

else:
    print(f"{num3} is largest among {num1} and {num2}")