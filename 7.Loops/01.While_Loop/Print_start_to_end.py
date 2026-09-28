# take start and end input by user
# start to end print using while loop

start = int(input("Enter start: "))
end = int(input("Enter End: "))

i = start
while i <= end:
    print(start ,end=" ")
    i += 1
print(f"After while loop, start value is {start}")