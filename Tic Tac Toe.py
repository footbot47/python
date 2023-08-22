import random
def drawBoard(board):
    print(' | |')
    print(''+board[7]+'|'+board[8]+'|'+board[9])
    print(' | |')
    print('------')
    print(' | |')
    print(''+board[4]+'|'+board[5]+'|'+board[6])
    print(' | |')
    print('------')
    print(' | |')
    print(''+board[1]+'|'+board[2]+'|'+board[3])
    print(' | |')
def inputPlayerLetter():
    letter=""
    while not(letter=='X' or letter=='O'):
        letter=input("Do you want to be X or O?").upper()
    if letter=='X':
        return['X','O']
    else:
        return['O','X']
def whoGoesFirst():#randomly chooses player who goes first
    if random.randint(0,1)==0:
        return'computer'
    else:
        return'player'
def playAgain():
    print('Do you want to play again?')
    return input().lower().startswith('y')
def makeMove(board,letter,move):
    board[move]=letter
def isWinner(bo,le):#returns true if you have won...........bo=board and le=letter
    return(bo[7]==le and bo[8]==le and bo[9]==le)#across the top
    (bo[4]==le and bo[5]==le and bo[6]==le)#across the middle
    (bo[1]==le and bo[2]==le and bo[3]==le)#across the bottom
    (bo[7]==le and bo[4]==le and bo[1]==le)#down the left
    (bo[8]==le and bo[5]==le and bo[2]==le)#down the middle
    (bo[9]==le and bo[6]==le and bo[3]==le)#down the right
    (bo[7]==le and bo[5]==le and bo[3]==le)#diagnol
    (bo[9]==le and bo[5]==le and bo[1]==le)#diagnol
def getBoardCopy(board):
    dupeBoard=[]
    for i in board:
        dupeBoard.append(i)
    return dupeBoard
def isSpaceFree(board,move):
    return board[move]==''
def getPlayerMove(board):#letting player make a move
    move=''
    while move not in '1,2,3,4,5,6,7,8,9'.split() or not isSpaceFree(board,int(move)):
        move=int(input("What's your next move?(1-9)"))
    return move
def chooseRandomMoveFromList(board,moveslist):#returns a move
    possiblemoves=[]
    for i in movesList():
        if isSpaceFree(board,i):
            possibleMoves.append(i)
    if len(possibleMoves)!=0:
        return random.choice(possibleMoves)
    else:
        return None
def getComputerMove(board,completter):
    if completter=='X':
        playerletter=='O'
    else:
        playerletter='X'
    #algorithm for tic tac toe:-
    for i in range(1,10):
        copy=getBoardcopy(board)
        if isSpaceFree(copy,i):
            makeMove(copy,playerLetter,i)
            if isWinner(copy,playerLetter):
                return i
    #making the computer go to the corner
    move=chooseRandomMoveFromList(board,[1,3,7,9])
    if move!=None:
        return move
    if isSpaceFree(board,5):#center
        return 5
    return chooseRandomMoveFromList(board,[2,4,6,8])#moving to the sides
def isBoardFull(board):#returns true if the space on the board is filled up
    for i in range(1,10):
        if isSpaceFree(board,i):
            return False
    return True
print("Welcome to Tic Tac Toe!")
while True:#resets board
    theBoard=['']*10
    playerletter,completter=playerletterinput(),completter=input=()
    turn=whoGoesFirst()
    print('The',+turn+'will go first')
    gameIsPlaying=True
    while gameIsPlaying:
        if turn=='player':#players turn
            drawBoard(theBoard)
            move=getPlayerMove(theBoard)
            makeMove(theBoard,playerLetter,move)
            if isWinner(theBoard,playerLetter):
                drawBoard(theBoard)
                print("You have won the game!")
                gameIsPlaying=False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie :(')
                    break
                else:
                    turn='computer'
        else:#computers turn
            move=getComputerMove(theBoard,completter)
            if isWinner(theBoard,completter):
                drawBoard(theBoard)
                print("The computer has beaten you!..You lose")
                gameIsPlaying=False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game is a tie!")
                else:
                    turn='player'
    if not playAgain():
        break
    


















    
