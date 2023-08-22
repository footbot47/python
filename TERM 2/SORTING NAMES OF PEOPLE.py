l=eval(input('Enter names'))
a=len(l)
j=l
for i in range(0,a-i-1):
    if l[j][0]>l[j+1][0]:
        l[j],l[j+1]=l[j+1],l[j]
print(l)



