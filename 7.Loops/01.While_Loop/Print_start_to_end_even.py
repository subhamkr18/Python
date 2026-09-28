# take start and end as user input
# print all even number b/w start and end
start = int(input("Enter start: ")) 
end = int(input("Enter end: "))

i= start

print(f"Even numbers form {start} to {end} are: ")
while i < end:
    if(i%2==0):
        print( i,end=" ")
    i += 1 
