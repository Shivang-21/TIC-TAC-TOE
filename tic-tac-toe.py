import random
board=[' ' for x in range(10)]
def insertLetter(letter,pos):
    board[pos]=letter
    
def spaceIsFree(pos):
    return board[pos]==' '

def isBoardFull(board):
    if board.count(' ')>1:
        return False
    else:
        return True
    
def printBoard(board):
    print('   |   |   ')
    print(' '+board[1]+' | '+board[2]+' | '+board[3]+' ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' '+board[4]+' | '+board[5]+' | '+board[6]+' ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' '+board[7]+' | '+board[8]+' | '+board[9]+' ')    
    print('   |   |   ')

def isWinner(b,l):
    return ((b[1]==l and b[2]==l and b[3]==l)or
            (b[4]==l and b[5]==l and b[6]==l)or
            (b[7]==l and b[8]==l and b[9]==l)or
            (b[1]==l and b[4]==l and b[7]==l)or
            (b[2]==l and b[5]==l and b[8]==l)or
            (b[3]==l and b[6]==l and b[9]==l)or
            (b[1]==l and b[5]==l and b[9]==l)or
            (b[3]==l and b[5]==l and b[7]==l))

def player1Move():
    run=True
    while run:
        move=int(input("Select a position to enter X between 1 and 9: "))
        try:
            if move>0 and move<10:
                if spaceIsFree(move):
                    insertLetter('X',move)
                    run=False
                else:
                    print("Sorry, this space is occupied")
            else:
                print("Please type a number between 1 & 9")
        except:
            print("Please type a number")

def player2Move():
    run=True
    while run:
        move=int(input("Select a position to enter X between 1 and 9: "))
        try:
            if move>0 and move<10:
                if spaceIsFree(move):
                    insertLetter('O',move)
                    run=False
                else:
                    print("Sorry, this space is occupied")
            else:
                print("Please type a number between 1 & 9")
        except:
            print("Please type a number")            
            
def selectRandom(lst):
    length=len(lst)
    r=random.randrange(0,length)
    return lst[r]
    
def computerMove():
    possiblemoves=[x for x,letter in enumerate(board) if letter==' ' and x!=0]
    move=0
    for let in ['O','X']:
        for i in possiblemoves:
            boardcopy=board[:]
            boardcopy[i]=let
            if isWinner(boardcopy,let):
                move=i
                return move
    cornersOpen=[]
    for i in possiblemoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if len(cornersOpen)>0:
        move=selectRandom(cornersOpen)
        return move
    if 5 in possiblemoves:
        move=5
        return move
    edgesOpen=[]
    for i in possiblemoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    if len(edgesOpen)>0:
        move=selectRandom(edgesOpen)
        return move

def main():
    print("Welcome to the game!")    
    c=input("Enter C to play against Computer and P to play against Player: ")
    printBoard(board)
    if c.upper()=='C':
        while not(isBoardFull(board)):
            if not (isWinner(board,'O')):
                print("Player's Turn")
                player1Move()
                printBoard(board)
            else:
                print("Sorry you loose")
                break
        
            if not (isWinner(board,'X')):                
                move=computerMove()
                if move!=None:
                    print("Computer's Turn")
                if move==0 or move==None:
                    print(" ")
                else:
                    insertLetter('O',move)
                    print("Computer placed O at position",move)
                    printBoard(board)
            else:
                print("You Win")
                break
        if isBoardFull(board):
            print("Game Tie")
    else:
        while not(isBoardFull(board)):
            if not (isWinner(board,'O')):
                print("First player's Turn")
                player1Move()
                printBoard(board)
            else:
                print("Player2 Wins")                      
                break
        
            if not (isWinner(board,'X')):
                print("Second player's Turn")
                player2Move()
                printBoard(board)                
            elif not (isBoardFull(board)):
                print("Player1 Wins")
                break            
        if isBoardFull(board):
             print("Game Tie")
        
            
while True:
    x=input("Do you want to play again:(y/n) ")
    if x.lower()=='y':
        board=[' ' for x in range(10)]
        print("------------------")
        main()
    else:
        break
    
            
            
              
              
                   
            
