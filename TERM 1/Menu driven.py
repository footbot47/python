#Menu driven
ans='y'
while ans==y:
    print("Select an option")
    print("1.Fibonacci series")
    print("2.Try something new?")
    ch=int(input("Enter a choice"))
    if ch==1:
        first=0
        second=1
        print(first)
        print(second)
        for i in range(1,100):
            third=first+second
            print(third)
            first,second=second,third
    elif ch==2:
        n=int(input("Enter a number"))
        a=1
        b=1
        c=2
        print(a,b,c,end="")
        for i in range(3,n):
            t=a+b*c
            print(t,end="")
            a=b
            b=c
            c=t
        else:
            print("Invalid input")
ans=input("Do you want to continue?(Y/N)")

            
