mydict={'a':27,'b':43,'c':25,'d':30}
vala=''
for i in mydict:
	if i>vala:
		vala=i
		valb=mydict[i]
print(vala)#line1
print(valb)#line2
print(30 in mydict)#line3
mylst=(mydict.items())
mylst.sort()#line4
print(mylst[-1])

