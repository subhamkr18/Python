"""
Take a student's marks as input. Print their grade based ont this scale:
* 90 and above -> A
* 75 to 89 -> B
* 60 to 74 -> C
* 40 to 59 -> D
* Below 40 -> F
"""
marks = int(input("Enter marks: "))

if marks >100 or marks < 0:
    print("Invalid marks")

elif marks > 90:
    print("Grade -> A")

elif marks >=75 and marks < 90:
    print("Grade -> B")

elif marks >= 60 and marks < 75:
    print("Grade -> C")

elif marks >= 40 and marks < 60:
    print("Grade -> D")

else:
    print("Grade -> F")