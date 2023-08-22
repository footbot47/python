n=int(input("Enter the number of months"))
c={}
for a in range(n):
    key=input("Enter month")
    values=int(input("Enter the number of days"))
    c[key]=values
print("The number of months and the days are:-")
print(c)
