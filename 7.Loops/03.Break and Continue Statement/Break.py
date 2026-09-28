# 1-10
# i = 5 loop stop 

i=1
while(i<=10):
    print(i,end=" ")
    if i==5:
        break
    i += 1

## 1-27

# break the loop when i % 19 =0
print("\n")
print("Print the number till it is divisible by 19:")
for i in range(1,28):
    if i % 19 == 0:
        break
    else:
        print(i,end=" ")