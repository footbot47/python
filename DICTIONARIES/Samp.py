n=int(input("Enter the number of items"))
c=0
for a in range(n):
    key=input("Enter the name of the item")
    value=int(input("Enter the price of the item"))
    c[key]=value

print("The items and their prices are:-")
print(c,"\t")
