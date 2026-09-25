""" 
A shop gives discounts based on purchase amount:
Above 5000 → 20% discount
Above 2000 → 10% discount
Above 1000 → 5% discount
1000 or below → no discount
"""
amount = int(input("Enter purchased amount: "))
# checking negative amount ionput
if(amount < 0 ):
    print(f"{amount } it's an invalid amount ")

# discount on or above 5000 -> 20%
elif(amount > 5000):
    print(f"you got Discount 20% : {amount * 0.20}")

# discount on or above 2000 and below 5000 -> 10%
elif(amount > 2000 and amount <= 5000):
    print(f" You got discount of 10% : {amount * 0.10}")

#discount on or above 1000 and below 2000 -> 5%
elif(amount > 1000 and amount <= 2000):
    print(f"You got discount of 5% : {amount * 0.05}")

# No discount below purchase of 1000
else:
    print("You don't get any discount sorry !")