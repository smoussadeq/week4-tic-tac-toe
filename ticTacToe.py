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
    
    
def startGame(startingPlayer, board):    # TO DO #################################################################    # Add comments to each line in this function to describe what           #    # is happening. You do not need to modify any of the Python code        #    #########################################################################    turn = startingPlayer # player turn to start    for i in range(9): # setting up the range of moves        printBoard(board) # printing out the board for the game        print('Turn for ' + turn + '. Move on which space?') # printing out the board at the start of each new turn        move = input() # getting the active player move        board[move] = turn # updating the game board        if( checkWinner(board, 'X') ): # checking if ‘X’ is the winner            print('X wins!') # printing out the winner            break # exiting the statement        elif ( checkWinner(board, 'O') ): # checking if ‘O’ is the winner            print('O wins!') # printing out the winner            break # exiting the statement
        if turn == 'X': # ‘X’ turn             turn = 'O' # ‘O’ turn        else: # or            turn = 'X' # ‘X’ turn             printBoard(board) # printing out the board    