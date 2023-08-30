import random
gameboard = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
currentplayer='X'
winner=None
gameRunning=True
def display():
    print(gameboard[0], '|', gameboard[1], '|', gameboard[2])
    print(gameboard[3], '|', gameboard[4], '|', gameboard[5])
    print(gameboard[6], '|', gameboard[7], '|', gameboard[8])
def userinput(gameboard):
    user1=int(input('enter the input(1-9) : '))
    if user1>0 and user1<=9 and gameboard[user1-1]:
        gameboard[user1-1]=currentplayer
    else:
        print(' take another input! ')
def horizontal(gameboard):
    global winner
    if gameboard[0]==gameboard[1]==gameboard[2]!='_':
        winner=gameboard[0]
        return True
    elif gameboard[3]==gameboard[4]==gameboard[5]!='_':
        winner = gameboard[3]
        return True
    elif gameboard[6]==gameboard[7]==gameboard[8]!='_':
        winner=gameboard[6]
        return True
def vertical(gameboard):
    global winner
    if gameboard[0]==gameboard[3]==gameboard[6]!='_':
        winner=gameboard[0]
        return True
    elif gameboard[1]==gameboard[4]==gameboard[7]!='_':
        winner=gameboard[1]
        return True
    elif gameboard[2]==gameboard[5]==gameboard[8]!='_':
        winner=gameboard[2]
        return True
def diagonal(gameboard):
    global winner
    if gameboard[0]==gameboard[4]==gameboard[8]!='_':
        winner=gameboard[0]
        return True
    elif gameboard[2]==gameboard[4]==gameboard[6]!='_':
        winner=gameboard[2]
        return True
def checkWin(gameboard):
    global gameRunning
    global winner
    horizontal(gameboard)
    vertical(gameboard)
    diagonal(gameboard)
    if horizontal(gameboard) or vertical(gameboard) or diagonal(gameboard)==True:
        print(display())
        gameRunning=False
        print('winner is', winner)
def checkTie(gameboard):
    global gameRunning
    if '_' not in gameboard:
        print('It''s a TIE!')
        gameRunning=False
def switchPlayer(gameboard):
    global currentplayer
    if currentplayer=='X':
        currentplayer='O'
    else:
        currentplayer='X'
def computer(gameboard):
    while currentplayer=='O':
        x=random.randint(0,8)
        if gameboard[x]=='_':
            gameboard[x]='O'
        elif gameboard[x]=='X':
            print('  take another input! ')
        switchPlayer(gameboard)
while gameRunning==True:
    display()
    userinput(gameboard)
    checkWin(gameboard)
    checkTie(gameboard)
    switchPlayer(gameboard)
    computer(gameboard)
display()  