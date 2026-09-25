"""
Take the user's age as input. Check and print whether they are eligible
to vote (age >= 18) and whether they are a senior citizen (age >= 60).
Print both results.

"""
age = int(input("Enter age: "))

# Checking whether they are senior citizen 
if(age>= 60):
    print("Person is Senior citizen and Eligibkle to vote")

elif(age>=18 and age<60):
    print("Person is eligible to vote")

else:
    print("Person is not eligible to vote")

