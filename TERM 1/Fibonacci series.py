#fibonacci
first=0
second=1
print(first,end=" ")
print(second,end=" ")
for i in range(1,100):
    third=first+second
    print(third,end=" ")
    first,second=second,third
