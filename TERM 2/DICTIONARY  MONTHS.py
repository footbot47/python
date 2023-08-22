n=int(input("Enter n"))
d={}
for i in range(n):
    keys=input('Enter month')
    val=int(input('Enter the number of days'))
    d[keys]=val
print(d)
m=input("Enter month")
print("The number of days in month",m,"=",d[m])
