age = int(input("Enter age: "))

# if age >= 18
# status ="Adult"
# else:
# status = "Minaor"

status = "Adult" if age >=18 else "Minor"

print(f"Your status is {status}")