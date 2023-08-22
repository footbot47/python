d={4:"number","a":"string",(1,2):"tuple"}
print("Dictionary contents")
for x in d.keys():
    print(x,':',d[x],end=' ')
    print(d[x]*3)
    print()
    
