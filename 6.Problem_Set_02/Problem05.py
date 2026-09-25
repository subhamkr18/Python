"""
Take a person's age and whether they have a valid ID (True/False) as input. They
can enter a venue only if they are 18 or older AND have a valid ID. Print the
appropriate message.

"""

age = int(input("Enter age: "))
valid_id = input("You have valid ID (True/False): ")

if age >= 18 and valid_id == "True":
    print("You are eligible")

else:
    print("You are not eligible")