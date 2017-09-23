"""
Wayne Tam
CS100-021
10/23/2016
Tic Tac Toe
"""
def playTwo():
    import turtle
    boardTurtle = turtle.Turtle()
    xTurtle = turtle.Turtle()
    oTurtle = turtle.Turtle()
    winTurtle = turtle.Turtle()
    boardTurtle.ht()
    xTurtle.ht()
    oTurtle.ht()
    winTurtle.ht()
    player = getPlayerNames()
    board = [0,1,2,3,4,5,6,7,8]
    drawboard(boardTurtle, 150)
    count = 0
    while gameOver(board) == '-':
        if count % 2 == 0:
            cellA = int(input('{} make a move, choosing from {} '.format(player[0],getMove(board))))
            if str(board[cellA]) not in 'xo':
                board[cellA] = 'x'
                drawX(xTurtle, cellA)
                xTurtle.pu()
                xTurtle.home()
                xTurtle.pd()
                count+=1
            else:
                print('Not a valid move')
                continue
        else:
            cellB = int(input('{} make a move, choosing from {} '.format(player[1],getMove(board))))
            if str(board[cellB]) not in 'xo': 
                board[cellB] = 'o'
                drawO(oTurtle, cellB)
                oTurtle.pu()
                oTurtle.home()
                oTurtle.pd()
                count+=1
            else:
                print('Not a valid move')
                continue
    if gameOver(board) == 'D':
        print('Draw')
    else:
        if gameOver(board) == 'X':
            print(player[0],'wins!')
        else:
            print(player[1],'wins!')
    winLine(winTurtle,board)

def playOne():
    import turtle
    boardTurtle = turtle.Turtle()
    xTurtle = turtle.Turtle()
    oTurtle = turtle.Turtle()
    winTurtle = turtle.Turtle()
    boardTurtle.ht()
    xTurtle.ht()
    oTurtle.ht()
    winTurtle.ht()
    board = [0,1,2,3,4,5,6,7,8]
    drawboard(boardTurtle, 150)
    count = 0
    while gameOver(board) == '-':
        if count % 2 == 0:
            cellA = int(input('Make a move, choosing from {} '.format(getMove(board))))
            if str(board[cellA]) not in 'xo':
                board[cellA] = 'x'
                drawX(xTurtle, cellA)
                xTurtle.pu()
                xTurtle.home()
                xTurtle.pd()
                count+=1
            else:
                print('Not a valid move. Please pick another move.')
                continue
        else:
            move = minimax(board,count)
            board[move] = 'o'
            drawO(oTurtle, move)
            oTurtle.pu()
            oTurtle.home()
            oTurtle.pd()
            count+=1
    if gameOver(board) == 'D':
        print('Draw')
    else:
        if gameOver(board) == 'X':
            print('You win!')
        else:
            print('You lose...')
    winLine(winTurtle,board)

def minimax(board, count):
    tempBoard = list(board)
    bestMove = 0
    bestScore = float('-inf')
    tempCount = count
    for move in getMove(board):     #combs through all possible 'O' turns, will make tree
        tempBoard[move] = 'o'       #projects next game state ('O' moves)
        moveScore = minMove(tempBoard, tempCount)
        if moveScore > bestScore:
            bestMove = move
            bestScore = moveScore
        tempBoard[move] = move
    return bestMove                 #AI will take the move that has the highest score

def minMove(board, count):  
    bestScore = float('inf')
    if gameOver(board) == 'X':  
        return count - 10           #returns depth of lost for AI
    elif gameOver(board) == 'O':
        return 10 - count           #returns depth of win for AI
    elif gameOver(board) == 'D':
        return 0                    #returns 0 when draw
    for move in getMove(board):     #combs through all possible next turn for 'X'
        board[move] = 'x'           #projects next game state ('X' moves)
        score = maxMove(board, count+1)
        if score < bestScore:
             bestScore = score
        board[move] = move
    return bestScore            

def maxMove(board, count):          
    bestScore = float('-inf')
    if gameOver(board) == 'X':
        return count - 10           #returns depth of lost for AI
    elif gameOver(board) == 'O':
        return 10 - count           #returns depth of win for AI
    elif gameOver(board) == 'D':
        return 0                    #returns 0 when draw
    for move in getMove(board):     #combs through all possible next turn for 'O'
        board[move] = 'o'           #projects next game state ('O' moves)
        score = minMove(board, count+1)     
        if score > bestScore:   
            bestScore = score
        board[move] = move
    return bestScore                

    
def getPlayerNames():
    aPlayer = input('Player one, what is your name? ')
    print(aPlayer,'will be X') 
    bPlayer = input('Player two, what is your name? ')
    print(bPlayer,'will be O') 
    names = (aPlayer, bPlayer)
    return names

def getMove(board):
    moves = []
    for move in board:
        if str(move) not in 'xo':
            moves.append(move)
    return moves

def drawboard(t, cellsize):
    t.speed(25)
    t.pu()
    t.fd(cellsize*1.5)
    t.lt(90)
    t.fd(cellsize/2)
    t.lt(90)
    t.pd()
    for i in range(4):
        t.fd(cellsize*3)
        t.pu()
        for i in range(2):
            t.rt(90)
            t.fd(cellsize)
        t.rt(90)
        t.pd()

def drawX(t, cell):
    t.speed(25)
    if cell == 0:
        t.pu()
        t.lt(90)
        t.fd(150)
        t.lt(90)
        t.fd(150)
        t.pd()
        drawMidline(t,100)
    elif cell == 1:
        t.pu()
        t.lt(90)
        t.fd(150)
        t.pd()
        drawMidline(t,100)
    elif cell == 2:
        t.pu()
        t.lt(90)
        t.fd(150)
        t.rt(90)
        t.fd(150)
        t.pd()
        drawMidline(t,100)
    elif cell == 3:
        t.pu()
        t.bk(150)
        t.pd()
        drawMidline(t,100)
    elif cell == 4:
        drawMidline(t,100)
    elif cell == 5:
        t.pu()
        t.fd(150)
        t.pd()
        drawMidline(t,100)
    elif cell == 6:
        t.pu()
        t.rt(90)
        t.fd(150)
        t.rt(90)
        t.fd(150)
        t.pd()
        drawMidline(t,100)
    elif cell == 7:
        t.pu()
        t.rt(90)
        t.fd(150)
        t.pd()
        drawMidline(t,100)
    elif cell == 8:
        t.pu()
        t.rt(90)
        t.fd(150)
        t.lt(90)
        t.fd(150)
        t.pd()
        drawMidline(t,100)
        

def drawO(t, cell):
    t.speed(25)
    if cell == 0:
        t.pu()
        t.lt(90)
        t.fd(150)
        t.lt(90)
        t.fd(150)
        t.pd()
        drawConcentric(t, 50)
    elif cell == 1:
        t.pu()
        t.lt(90)
        t.fd(150)
        t.pd()
        drawConcentric(t, 50)
    elif cell == 2:
        t.pu()
        t.lt(90)
        t.fd(150)
        t.rt(90)
        t.fd(150)
        t.pd()
        drawConcentric(t, 50)
    elif cell == 3:
        t.pu()
        t.bk(150)
        t.pd()
        drawConcentric(t, 50)
    elif cell == 4:
        drawConcentric(t, 50)
    elif cell == 5:
        t.pu()
        t.fd(150)
        t.pd()
        drawConcentric(t, 50)
    elif cell == 6:
        t.pu()
        t.rt(90)
        t.fd(150)
        t.rt(90)
        t.fd(150)
        t.pd()
        drawConcentric(t, 50)
    elif cell == 7:
        t.pu()
        t.rt(90)
        t.fd(150)
        t.pd()
        drawConcentric(t, 50)
    elif cell == 8:
        t.pu()
        t.rt(90)
        t.fd(150)
        t.lt(90)
        t.fd(150)
        t.pd()
        drawConcentric(t, 50)  
        
def drawConcentric(t, radius):
    t.speed(25)
    t.pu()
    t.fd(radius)
    t.lt(90)
    t.pd()
    t.circle(radius)

def drawMidline(t, length):
    t.speed(25)
    t.lt(45)
    t.fd(length/2)
    t.lt(135)
    t.pu()
    t.fd(length/2**(1/2))
    t.pd()
    t.lt(135)
    t.fd(length)
    t.pu()
    t.rt(135)
    t.fd(length/2**(1/2))
    t.pd()
    t.rt(135)
    t.fd(length/2)

def gameOver(board):
    if board[0] == 'x' and board[1] == 'x' and board[2] == 'x':
        return 'X'
    elif board[0] == 'x' and board[3] == 'x' and board[6] == 'x':
        return 'X'
    elif board[0] == 'x' and board[4] == 'x' and board[8] == 'x':
        return 'X'
    elif board[1] == 'x' and board[4] == 'x' and board[7] == 'x':
        return 'X'
    elif board[2] == 'x' and board[5] == 'x' and board[8] == 'x':
        return 'X'
    elif board[2] == 'x' and board[4] == 'x' and board[6] == 'x':
        return 'X'
    elif board[3] == 'x' and board[4] == 'x' and board[5] == 'x':
        return 'X'
    elif board[6] == 'x' and board[7] == 'x' and board[8] == 'x':
        return 'X'
    elif board[0] == 'o' and board[1] == 'o' and board[2] == 'o':
        return 'O'
    elif board[0] == 'o' and board[3] == 'o' and board[6] == 'o':
        return 'O'
    elif board[0] == 'o' and board[4] == 'o' and board[8] == 'o':
        return 'O'
    elif board[1] == 'o' and board[4] == 'o' and board[7] == 'o':
        return 'O'
    elif board[2] == 'o' and board[5] == 'o' and board[8] == 'o':
        return 'O'
    elif board[2] == 'o' and board[4] == 'o' and board[6] == 'o':
        return 'O'
    elif board[3] == 'o' and board[4] == 'o' and board[5] == 'o':
        return 'O'
    elif board[6] == 'o' and board[7] == 'o' and board[8] == 'o':
        return 'O'
    if board.count('o') + board.count('x') == 9:
        return 'D'
    else:
        return '-'
    
def winLine(t, board):
    if (board[0] == 'x' and board[1] == 'x' and board[2] == 'x') or (board[0] == 'o' and board[1] == 'o' and board[2] == 'o'):
        t.pu()
        t.lt(90)
        t.fd(150)
        t.rt(90)
        t.fd(225)
        t.pd()
        t.bk(450)
    elif (board[0] == 'x' and board[3] == 'x' and board[6] == 'x') or (board[0] == 'o' and board[3] == 'o' and board[6] == 'o'):
        t.pu()
        t.bk(150)
        t.lt(90)
        t.fd(225)
        t.pd()
        t.bk(450)
    elif (board[0] == 'x' and board[4] == 'x' and board[8] == 'x') or (board[0] == 'o' and board[4] == 'o' and board[8] == 'o'):
        t.pu()
        t.lt(135)
        t.fd(318.198)
        t.pd()
        t.bk(636.3961)
    elif (board[1] == 'x' and board[4] == 'x' and board[7] == 'x') or (board[1] == 'o' and board[4] == 'o' and board[7] == 'o'):
        t.pu()
        t.lt(90)
        t.fd(225)
        t.pd()
        t.bk(450)
    elif (board[2] == 'x' and board[5] == 'x' and board[8] == 'x') or (board[2] == 'o' and board[5] == 'o' and board[8] == 'o'):
        t.pu()
        t.fd(150)
        t.lt(90)
        t.fd(225)
        t.pd()
        t.bk(450)
    elif (board[2] == 'x' and board[4] == 'x' and board[6] == 'x') or (board[2] == 'o' and board[4] == 'o' and board[6] == 'o'):
        t.pu()
        t.lt(45)
        t.fd(318.198)
        t.pd()
        t.bk(636.3961)
    elif (board[3] == 'x' and board[4] == 'x' and board[5] == 'x') or (board[3] == 'o' and board[4] == 'o' and board[5] == 'o'):
        t.pu()
        t.fd(225)
        t.pd()
        t.bk(450)
    elif (board[6] == 'x' and board[7] == 'x' and board[8] == 'x') or (board[6] == 'o' and board[7] == 'o' and board[8] == 'o'):
        t.pu()
        t.rt(90)
        t.fd(150)
        t.rt(90)
        t.fd(225)
        t.pd()
        t.bk(450)

playTwo()
        
