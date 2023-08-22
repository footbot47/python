import time
name=input("What's your name?")
print("Hello",name,"Time to play hangman!")


print("Start guessing.....")

word="secret"
guesses=''
turns=10
while turns>0:
    failed=0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed=failed+1
    if failed==0:
        print("You won")
        break
guess=input("Enter your guesses")
guesses=guesses+guess
if guess not in word:
    turns-=1
    print("Wrong guess")
    print("You have",turns,"more guesses")
if turns==0:
    print("You loose")
    

        
      

