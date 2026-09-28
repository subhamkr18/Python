# 1-10
# i = 7 continue
i=1
while(i<=10):
    i+=1
    if i == 7:
        continue
    print(i,end=" ")

print("\n")

#print odd number from 1-51 using continue statement
print("Odd no from 1-50 are: ")

for i in range(1,51):
    if i%2==0:
        continue
    print(i,end=" ")