l=[]
r=int(input('Enter rows'))
c=int(input('Enter columns'))
for i in range(r):
    row=[]
    for j in range(c):
        e=int(input('Enter element'))
        row.append(e)
    l.append(row)

for i in range(r):
    for j in range(c):
        print(l[i][j],end=' ')
    print()

print('middle row')
m=r//2

print(l[m])

        
