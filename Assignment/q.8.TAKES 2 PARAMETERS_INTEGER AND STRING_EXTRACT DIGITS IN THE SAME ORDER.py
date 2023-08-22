def s(integer,string):
    st=""
    for i in string:
        if i.isdigit():
            st+=str(i)
    if st=="":
        print("extracted digits=0")
    else:
        print("the digits in the string=",int(st))
    if st!="":
        inte= integer+int(st)
    elif st=="":
        inte=integer+0
    print("calculated integer from digits of string and the integer parameter:")
    return(inte)
integer=int(input("enter your integer:"))
string=input("enter string:")
print(s(integer,string))
#by pradipti class xii

    
            
