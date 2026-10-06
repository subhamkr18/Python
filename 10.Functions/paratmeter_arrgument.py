# 3 int as a parameter, print the total
def add(a,b,c):
    print(f"Totalis: {a+b+c}")

add(5,6,9)



# ask name,age and gender print it

def greet(name,age,gender):
    print(f"hey {name} your age is {age} and your gender is {gender}")

n=input("Enter name: ")
a= int(input("Enter age: "))
g= (input("Enter Gender: "))

greet(n,a,g)