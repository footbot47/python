s=input("Enter the word")
c=input("Enter the character")
n=""
for i in range(0,len(s)):
    if s[i]==c:
        n+=s[i].upper()
    else:
        n+=s[i].lower()
print("Altered string=",n)
