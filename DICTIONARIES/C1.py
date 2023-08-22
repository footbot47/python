n=int(input("Enter the number of teams"))
c={}
l={}
for a in range(n):
    key=input("Enter team name")
    value=int(input("Enter the number of wins"))
    c[key]=value
    value1=int(input("Enter the number of losses"))
    l[key]=value1

print("Wins:-")
print(c)
print("The losses:-")
print(l)

