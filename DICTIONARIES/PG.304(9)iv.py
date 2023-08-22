list1=[2,3,3,2,5,3,2,5,1,1]
cnts={}
ct=0
lst=[]
for num in list1:
    if num not in lst:
        lst.append(num)
        cnts[num]=0
    ct=ct+1
    cnts[num]=cnts[num]+1
print(cnts)
for key in cnts.keys():
    cnts[key]=key*cnts[key]
print(cnts)
