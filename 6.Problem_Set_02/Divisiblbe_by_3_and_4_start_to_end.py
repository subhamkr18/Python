# print start to  end, numbers which are divisible by 3 and 4

start = int(input("Enter start: "))
end = int(input("Enter end: "))

i = start
print(f"number which are divisible by 3 and 4 from {start} to {end} are: ")
while  i < end:
    if i % 3 == 0 and i % 4 ==0:
        print(i,end=" ")
    i += 1