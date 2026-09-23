name="Subham"
age=20
gender="male"

print("Hello",name," you age is", age," and gender is ",gender)

print("Hello "+ name+"your gender is"+ gender)
print(name, age, gender)

# sep separates the print statement by default sep separates with space
print(name,age,gender,sep="")

# end use to end the line we can pass something by which we want to end 
print(name, age , end=" .")
print(gender)

# F-strings
print(f"Your name is {name}, age is {age} years and gender is {gender}")