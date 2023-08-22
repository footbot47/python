def palin(x):
    if len(x)==1:
        return True
    elif x[0]==x[-1]:
        return palin(x[1:-1])
    else:
        return False

x=input('Enter a string')
ans=palin(x)
if ans==False:
    print('no palin')
else:
    print('palin')
    
