a=input('Enter a string')
c=input('Enter a character')
for i in range(0,len(a)):
    if a[i]==c:
        print('Character',c,'is at index',i)
    else:
        print(c,'does not exist in position',i)
        
