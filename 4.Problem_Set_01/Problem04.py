"""
A student scored marks in 3 subjects. Take all three as input,
calculate the total and average, and print both using an f-string
"""

Subject1 = int(input("Enter Subject 1 marks: "))
Subject2 = int(input("Enter Subject 2 marks: "))
Subject3 = int(input("Enter Subject 3 marks: "))

# Calculating and printing Total marks
print(f"Total marks is: {Subject1+Subject2+Subject3}")

#Calculating and printing Average marks

print(f" Average marks is:{(Subject1+Subject2+Subject3)/3}")