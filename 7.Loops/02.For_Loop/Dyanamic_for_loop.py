# print atart to end
start = int(input("Enter start: "))
end = int(input("Enter end: "))

print(f"printing from {start} to {end}: ")
for i in range(start,end+1):
    print(i,end=" ")

print("\n")

total =0

for i in range(start,end+1):
    total += i

print(f"Sum of all from {start}-{end} : ",total)