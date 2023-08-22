n=int(input("Enter a number"))
n1=0
n2=n
while n2!=0:
    n1=10*n1+n2%10
    n2=n2//10
if n==n1:
    print(n,"is a palindrome")
else:
    print(n,"is not a palindrome")
