# 10 to 1
# step -1
for i in range(10,1,-1):
    print(i,end=" ")

print("\n using step -3 ")
#  step -3
for i in range(10,1,-3):
    print(i,end=" ")

# printing divisible by 2 and 3 from 100 to 1
# step -1
print("\n Even no from 100 - 1: ")
for i in range(100,0,-1):
    if i % 2 == 0 and i % 3 == 0:
        print(i, end=" ")