def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R']) 
   
def checkWinner(board, player):    
    print('Checking if ' + player + ' is a winner...')
    # Given a board and a player’s letter, this function returns True if that player has won.
    return ((board['top-L'] == player and board['top-M'] == player and board['top-R'] == player) or # across the top
    (board['mid-L'] == player and board['mid-M'] == player and board['mid-R'] == player) or # across the middle
    (board['low-L'] == player and board['low-M'] == player and board['low-R'] == player) or # across the bottom
    (board['top-R'] == player and board['mid-R'] == player and board['low-R'] == player) or # down the left side
    (board['top-M'] == player and board['mid-M'] == player and board['low-M'] == player) or # down the middle
    (board['top-L'] == player and board['mid-L'] == player and board['low-L'] == player) or # down the right side
    (board['top-L'] == player and board['mid-M'] == player and board['low-R'] == player) or # diagonal
    (board['top-R'] == player and board['mid-M'] == player and board['low-L'] == player)) # diagonal
    
    
def startGame(startingPlayer, board):    # TO DO #################################################################    # Add comments to each line in this function to describe what           #    # is happening. You do not need to modify any of the Python code        #    #########################################################################    turn = startingPlayer    for i in range(9):        printBoard(board)        print('Turn for ' + turn + '. Move on which space?')        move = input()        board[move] = turn        if( checkWinner(board, 'X') ):            print('X wins!')            break        elif ( checkWinner(board, 'O') ):            print('O wins!')            break   
        if turn == 'X':            turn = 'O'        else:            turn = 'X'            printBoard(board)    