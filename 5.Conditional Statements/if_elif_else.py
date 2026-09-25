"""
if marks > 90 -A
marks >=80 <90 -B
same with other grade 

if input marks > 100 or <0 - invalid input
"""
marks = int(input("Enter marks: "))

if marks >100 or marks<0:
    print("invalid marks input")

elif marks >=90:
    print("Grade A")

elif marks>=80 and marks<90:
    print("Grade B")

elif marks >=70 and marks<80:
    print("Grade C")

elif marks >=60 and marks < 70:
    print("Grade D")

elif marks >= 50 and marks <60:
    print("Grade E")

elif marks >=35 and marks <50:
    print("Grade P -Pass")

else:
    print("Sorry You got Grade F - Fail")