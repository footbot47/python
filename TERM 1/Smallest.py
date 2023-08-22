n=int(input("Enter the limit"))
a=int(input("Enter the first number"))
min=a
print("second number onwards")
for i in range(1,n):
    a=int(input("Enter a number"))
if a<min:
    min=a
print("Smallest number=",min)
