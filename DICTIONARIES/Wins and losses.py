d={}
n=int(input("Enter the number of teams"))
for i in range(n):
    keys=input("Enter team name")
    wins=int(input("Enter wins"))
    losses=int(input("Enter losses"))
    d[keys]=(wins,losses)
print(d)
t=input("Enter the team name")
if t in d:
    print("Winning=",100*d[t][0]/(d[t][0]+d[t][1]))
else:
    print("Team name",b,"not found")
    
