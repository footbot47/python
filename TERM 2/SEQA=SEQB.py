t1=eval(input("Enter the first tuple"))
t2=eval(input("Enter the second tuple"))
f=True
for i in t1:
    if i not in t2:
        f=False
        break
print(f)
