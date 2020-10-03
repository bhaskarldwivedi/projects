import random

def DisplayBoard(board):
    for i in range(3):
        print(board[i])
        
    
def EnterMove(board):
    usermove = int(input("Enter your move:"))
    for i in range(3):
        for j in range(3):
            if board[i][j] == usermove and board[i][j]!="0" and board[i][j]!="x":   
                board[i][j] = "0"
    return board

def MakeListOfFreeFields(board):
    FreeFields = ()
    for i in range(3):
        for j in range(3):
            if board[i][j] != "x" and board[i][j] != "0":
                FreeFields = FreeFields + (i,j)
    data = len(FreeFields)
    table = tuple(FreeFields[n:n+2] for n in range(0,data,2))
    return table
   
def DrawMove(board):
    FreeFields = MakeListOfFreeFields(board)
    #print(FreeFields)
    if len(FreeFields) != 0 :
        Compmove = random.randrange(len(FreeFields))
        
        CompMove = list(FreeFields[Compmove])
        
        board[CompMove[0]][CompMove[1]] = "x"
        return board
    elif len(FreeFields) == 0:
        print("Game is draw")
        
    
        
def VictoryFor(board, sign):
    
    for i in range(3):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            return True
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            return True
        
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True

 
    return False
     

            
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
#


newlist =  [[i for i in range(1,4)] for j in range(1,4)]

x = 1
for i in range(3):
    for j in range(3):
        #if x == 5:
            #newlist[i][j] = "x"
        #else:
            #newlist[i][j] = x
        newlist[i][j] = x
        x = x + 1
        
#print(newlist[i])

board = newlist[:]

DisplayBoard(board)

victory = False

while victory == False:

    board = EnterMove(board)

    victory = VictoryFor(board, "0")

    DisplayBoard(board)
    
    if victory:
        print("user wins")
        break

    MakeListOfFreeFields(board)

    DrawMove(board)

    victory = VictoryFor(board, "x")

    DisplayBoard(board)

    if victory:
        print("computer wins")
        break

    if len(MakeListOfFreeFields(board)) == 0:
        victory = True



