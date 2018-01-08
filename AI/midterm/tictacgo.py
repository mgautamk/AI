
__author__ = 'mgautam'
import sys
sys.setrecursionlimit(1000000)
import random
import copy

#----------------------------------------------------------------------------
#Author: Mahesh Gautam
#Class: CS 480 AI
#Instructor: Dr. Bala RaviKumar
#Assignment: Midterm 1
#Description: Implementation of Minmax algorithm and Alpha beta pruning
# on Tic Tac Toe two player game where player wins if they have no boxes
#with same Xs or Os in same row or column and have acquired all columns
#------------------------------------------------------------------------------

def makeMove(board, player, location):
    gridlist = list(board)
    gridlist[location] = player
    return ''.join(gridlist)

#Different boards for test cases
board0 = [
    '2', '0', '0', '2',
    '2', '1', '0', '1',
    '2', '0', '0', '1',
    '0', '0', '0', '1']

board1 = [
    '1', '2', '0', '0',
    '1', '0', '2', '0',
    '2', '0', '0', '1',
    '2', '0', '0', '1']

board2 = [
    '1', '2', '2', '0',
    '1', '1', '2', '0',
    '0', '0', '0', '0',
    '2', '1', '0', '0']

board3 = [
    '2', '0', '2', '0',
    '1', '0', '0', '1',
    '1', '2', '0', '0',
    '0', '0', '0', '1']

#prints the board
def show(board):
    print (board[0], '|', board[1], '|',board[2],'|',board[3])
    print ('--------------')
    print (board[4], '|', board[5], '|',board[6],'|',board[7])
    print ('--------------')
    print (board[8], '|', board[9], '|',board[10],'|',board[11])
    print ('--------------')
    print (board[12], '|', board[13],'|',board[14],'|',board[15])

#Winning combinations
winning_combos = [
    [0, 5, 10, 15],[0, 5, 14, 11],[0, 6, 9, 15], [0, 6, 11, 13], [0, 7, 9, 14] , [0, 7, 13, 11], [0, 9, 6, 15],
    [0, 9, 14, 7],[0, 10, 4, 15], [0, 10, 12, 7], [0, 11, 4, 13],[0, 11, 5, 12], [0, 13, 4, 11], [0, 13, 8, 7],
    [0, 14, 4, 11], [0, 14, 8, 7], [0, 15, 5, 10], [0, 15, 9, 6],]

#available moves where 0's are placed
def availableMoves(board):
    return [k for k, v in enumerate(board) if v == '0']

def availablePositions(board):
        locations = []
        loc = []
        for row in range(4):
                for col in range(4):
                        if (int(board[row][col]) == 0):
                                loc = [row, col]
                                locations.append(copy.copy(loc))
        return locations

#Global variables
x_rows = [] #x rows
x_cols = [] #x columns
o_rows = [] #o rows
o_cols = [] #o columns

#Question number ii
#This function returns score -100 for win of 0(2nd player),
# 100 for win of X, -1 for invalid board and number of ways
#player 1 can win vs player 2 otherwise
def evaluate_board(board):
    x_win = False
    o_win = False
    x_count = 0
    o_count = 0
    try:
        row_index = 0
        for row in board:
            col_index = 0
            for col in row:
                if col == '2':
                    x_count += 1  #x_count
                    if row_index not in x_rows:
                        x_rows.append(row_index)  #xrows append
                    if col_index not in x_cols:
                        x_cols.append(col_index)
                elif col == '1':
                    o_count += 1 #o_count
                    if row_index not in o_rows:
                        o_rows.append(row_index)
                    if col_index not in o_cols:
                        o_cols.append(col_index)
                col_index += 1
            row_index += 1
        if len(x_rows) == 4 and len(x_cols) == 4: #Is complete for 2 or X
            x_win = True
        if len(o_rows) == 4 and len(o_cols) == 4: # IS complete for 1 or O
            o_win = True
    except Exception as e:
        print (e)
        return -1
    if o_count != x_count and o_count - 1 != x_count:
        #print ("counts %s %s" % (str(x_count), str(o_count)))
        return -1
    if x_win:
        if o_win:
            return 0.5
        else:
            return 100  #x or 2 win
    elif o_win:
        return -100  #o or 1 win
    else:
        #print ("Number of ways player 1 can win vs o can win")
        diff = len(x_rows) - len(o_cols)
        #print (diff)
        return diff
        #return -2

def staticEval(board):
	# We need 4 copies of the possible winning combinations
	# 2 to keep track if player 1 or 2 have won
	# and 2 to calculate the amount of ways player 1 and 2 can still win
	p1wins = [ 
	  [ [ 0,0 ], [ 1,1 ], [ 2,2 ], [ 3,3 ] ],
	  [ [ 0,0 ], [ 1,1 ], [ 2,3 ], [ 3,2 ] ],
	  [ [ 0,0 ], [ 1,2 ], [ 2,1 ], [ 3,3 ] ],
	  [ [ 0,0 ], [ 1,2 ], [ 2,3 ], [ 3,1 ] ],
	  [ [ 0,0 ], [ 1,3 ], [ 2,1 ], [ 3,2 ] ],
	  [ [ 0,0 ], [ 1,3 ], [ 2,2 ], [ 3,1 ] ],
	  [ [ 0,1 ], [ 1,0 ], [ 2,2 ], [ 3,3 ] ],
	  [ [ 0,1 ], [ 1,0 ], [ 2,3 ], [ 3,2 ] ],
	  [ [ 0,1 ], [ 1,2 ], [ 2,0 ], [ 3,3 ] ],
	  [ [ 0,1 ], [ 1,2 ], [ 2,3 ], [ 3,0 ] ],
	  [ [ 0,1 ], [ 1,3 ], [ 2,0 ], [ 3,2 ] ],
	  [ [ 0,1 ], [ 1,3 ], [ 2,2 ], [ 3,0 ] ],
	  [ [ 0,2 ], [ 1,0 ], [ 2,1 ], [ 3,3 ] ],
	  [ [ 0,2 ], [ 1,0 ], [ 2,3 ], [ 3,1 ] ],
	  [ [ 0,2 ], [ 1,1 ], [ 2,0 ], [ 3,3 ] ],
	  [ [ 0,2 ], [ 1,1 ], [ 2,3 ], [ 3,0 ] ],
	  [ [ 0,2 ], [ 1,3 ], [ 2,0 ], [ 3,1 ] ],
	  [ [ 0,2 ], [ 1,3 ], [ 2,1 ], [ 3,0 ] ],
	  [ [ 0,3 ], [ 1,0 ], [ 2,1 ], [ 3,2 ] ],
	  [ [ 0,3 ], [ 1,0 ], [ 2,2 ], [ 3,1 ] ],
	  [ [ 0,3 ], [ 1,1 ], [ 2,0 ], [ 3,2 ] ],
	  [ [ 0,3 ], [ 1,1 ], [ 2,2 ], [ 3,0 ] ],
	  [ [ 0,3 ], [ 1,2 ], [ 2,0 ], [ 3,1 ] ],
	  [ [ 0,3 ], [ 1,2 ], [ 2,1 ], [ 3,0 ] ],
	]
	p2wins = [ 
	  [ [ 0,0 ], [ 1,1 ], [ 2,2 ], [ 3,3 ] ],
	  [ [ 0,0 ], [ 1,1 ], [ 2,3 ], [ 3,2 ] ],
	  [ [ 0,0 ], [ 1,2 ], [ 2,1 ], [ 3,3 ] ],
	  [ [ 0,0 ], [ 1,2 ], [ 2,3 ], [ 3,1 ] ],
	  [ [ 0,0 ], [ 1,3 ], [ 2,1 ], [ 3,2 ] ],
	  [ [ 0,0 ], [ 1,3 ], [ 2,2 ], [ 3,1 ] ],
	  [ [ 0,1 ], [ 1,0 ], [ 2,2 ], [ 3,3 ] ],
	  [ [ 0,1 ], [ 1,0 ], [ 2,3 ], [ 3,2 ] ],
	  [ [ 0,1 ], [ 1,2 ], [ 2,0 ], [ 3,3 ] ],
	  [ [ 0,1 ], [ 1,2 ], [ 2,3 ], [ 3,0 ] ],
	  [ [ 0,1 ], [ 1,3 ], [ 2,0 ], [ 3,2 ] ],
	  [ [ 0,1 ], [ 1,3 ], [ 2,2 ], [ 3,0 ] ],
	  [ [ 0,2 ], [ 1,0 ], [ 2,1 ], [ 3,3 ] ],
	  [ [ 0,2 ], [ 1,0 ], [ 2,3 ], [ 3,1 ] ],
	  [ [ 0,2 ], [ 1,1 ], [ 2,0 ], [ 3,3 ] ],
	  [ [ 0,2 ], [ 1,1 ], [ 2,3 ], [ 3,0 ] ],
	  [ [ 0,2 ], [ 1,3 ], [ 2,0 ], [ 3,1 ] ],
	  [ [ 0,2 ], [ 1,3 ], [ 2,1 ], [ 3,0 ] ],
	  [ [ 0,3 ], [ 1,0 ], [ 2,1 ], [ 3,2 ] ],
	  [ [ 0,3 ], [ 1,0 ], [ 2,2 ], [ 3,1 ] ],
	  [ [ 0,3 ], [ 1,1 ], [ 2,0 ], [ 3,2 ] ],
	  [ [ 0,3 ], [ 1,1 ], [ 2,2 ], [ 3,0 ] ],
	  [ [ 0,3 ], [ 1,2 ], [ 2,0 ], [ 3,1 ] ],
	  [ [ 0,3 ], [ 1,2 ], [ 2,1 ], [ 3,0 ] ],
	]
	p1remaining = [ 
	  [ [ 0,0 ], [ 1,1 ], [ 2,2 ], [ 3,3 ] ],
	  [ [ 0,0 ], [ 1,1 ], [ 2,3 ], [ 3,2 ] ],
	  [ [ 0,0 ], [ 1,2 ], [ 2,1 ], [ 3,3 ] ],
	  [ [ 0,0 ], [ 1,2 ], [ 2,3 ], [ 3,1 ] ],
	  [ [ 0,0 ], [ 1,3 ], [ 2,1 ], [ 3,2 ] ],
	  [ [ 0,0 ], [ 1,3 ], [ 2,2 ], [ 3,1 ] ],
	  [ [ 0,1 ], [ 1,0 ], [ 2,2 ], [ 3,3 ] ],
	  [ [ 0,1 ], [ 1,0 ], [ 2,3 ], [ 3,2 ] ],
	  [ [ 0,1 ], [ 1,2 ], [ 2,0 ], [ 3,3 ] ],
	  [ [ 0,1 ], [ 1,2 ], [ 2,3 ], [ 3,0 ] ],
	  [ [ 0,1 ], [ 1,3 ], [ 2,0 ], [ 3,2 ] ],
	  [ [ 0,1 ], [ 1,3 ], [ 2,2 ], [ 3,0 ] ],
	  [ [ 0,2 ], [ 1,0 ], [ 2,1 ], [ 3,3 ] ],
	  [ [ 0,2 ], [ 1,0 ], [ 2,3 ], [ 3,1 ] ],
	  [ [ 0,2 ], [ 1,1 ], [ 2,0 ], [ 3,3 ] ],
	  [ [ 0,2 ], [ 1,1 ], [ 2,3 ], [ 3,0 ] ],
	  [ [ 0,2 ], [ 1,3 ], [ 2,0 ], [ 3,1 ] ],
	  [ [ 0,2 ], [ 1,3 ], [ 2,1 ], [ 3,0 ] ],
	  [ [ 0,3 ], [ 1,0 ], [ 2,1 ], [ 3,2 ] ],
	  [ [ 0,3 ], [ 1,0 ], [ 2,2 ], [ 3,1 ] ],
	  [ [ 0,3 ], [ 1,1 ], [ 2,0 ], [ 3,2 ] ],
	  [ [ 0,3 ], [ 1,1 ], [ 2,2 ], [ 3,0 ] ],
	  [ [ 0,3 ], [ 1,2 ], [ 2,0 ], [ 3,1 ] ],
	  [ [ 0,3 ], [ 1,2 ], [ 2,1 ], [ 3,0 ] ],
	]
	p2remaining = [ 
	  [ [ 0,0 ], [ 1,1 ], [ 2,2 ], [ 3,3 ] ],
	  [ [ 0,0 ], [ 1,1 ], [ 2,3 ], [ 3,2 ] ],
	  [ [ 0,0 ], [ 1,2 ], [ 2,1 ], [ 3,3 ] ],
	  [ [ 0,0 ], [ 1,2 ], [ 2,3 ], [ 3,1 ] ],
	  [ [ 0,0 ], [ 1,3 ], [ 2,1 ], [ 3,2 ] ],
	  [ [ 0,0 ], [ 1,3 ], [ 2,2 ], [ 3,1 ] ],
	  [ [ 0,1 ], [ 1,0 ], [ 2,2 ], [ 3,3 ] ],
	  [ [ 0,1 ], [ 1,0 ], [ 2,3 ], [ 3,2 ] ],
	  [ [ 0,1 ], [ 1,2 ], [ 2,0 ], [ 3,3 ] ],
	  [ [ 0,1 ], [ 1,2 ], [ 2,3 ], [ 3,0 ] ],
	  [ [ 0,1 ], [ 1,3 ], [ 2,0 ], [ 3,2 ] ],
	  [ [ 0,1 ], [ 1,3 ], [ 2,2 ], [ 3,0 ] ],
	  [ [ 0,2 ], [ 1,0 ], [ 2,1 ], [ 3,3 ] ],
	  [ [ 0,2 ], [ 1,0 ], [ 2,3 ], [ 3,1 ] ],
	  [ [ 0,2 ], [ 1,1 ], [ 2,0 ], [ 3,3 ] ],
	  [ [ 0,2 ], [ 1,1 ], [ 2,3 ], [ 3,0 ] ],
	  [ [ 0,2 ], [ 1,3 ], [ 2,0 ], [ 3,1 ] ],
	  [ [ 0,2 ], [ 1,3 ], [ 2,1 ], [ 3,0 ] ],
	  [ [ 0,3 ], [ 1,0 ], [ 2,1 ], [ 3,2 ] ],
	  [ [ 0,3 ], [ 1,0 ], [ 2,2 ], [ 3,1 ] ],
	  [ [ 0,3 ], [ 1,1 ], [ 2,0 ], [ 3,2 ] ],
	  [ [ 0,3 ], [ 1,1 ], [ 2,2 ], [ 3,0 ] ],
	  [ [ 0,3 ], [ 1,2 ], [ 2,0 ], [ 3,1 ] ],
	  [ [ 0,3 ], [ 1,2 ], [ 2,1 ], [ 3,0 ] ],
	]
	for row in range(4):
		for col in range(4):
	#		print "row: ", row
	#		print "col: ", col
			if (int(board[row][col]) == 1):
				temp = [ row , col ] # package location
				for p1 in p1wins: # Iterate through the winning combinations
					if temp in p1: # If our location is in the winning combination
						p1.remove(temp) # If it is remove it
				for p2 in p2remaining[:]: # Iterate through the opponents winning combinations
					if temp in p2: # If our location is in the winning combinations
						if p2 in p2remaining: # If this combination still exists as a winning combination
							p2remaining.remove(p2) # If it is remove it

			elif (int(board[row][col]) == 2):
				temp = [ row, col ] # package location
				for p2 in p2wins: # Iterate through the winning combinations
					if temp in p2: # If our location is in the winning combination
						p2.remove(temp) # If it is remove it
				for p1 in p1remaining[:]: # Iterate through the opponents winning combinations
					if temp in p1: # If our location is in the winning combinations
						if p1 in p1remaining: # If this combination still exists as a winning combination
							p1remaining.remove(p1)	# if is is remove it
	for win in p1wins:
		if len(win) == 0: # Player 1 has won
			return 100
	for win in p2wins:
		if len(win) == 0: # Player 2 has won
			return -100
	return len(p1remaining) - len(p2remaining) # Return the amount of ways P1 can win - amount of ways P2 can win


#This function returns the enemy player
def get_enemy(player):
    if player == '1':
        return '2'
    else:
        return '1'

#Question number i
#Minimax function, returns the best move and the value of board
#if board is complete or invalid
def minimax(board,player):
    val = evaluate_board(board)
    minimax.nodes_explored += 1
    if val == 100:
        print ("win for X")
        return 1
    elif val == 0.5:
        print ("Tie")
        return 0.5
    elif val == -100:
        print ("win for O")
        return 0
    elif val == -1:
        print ("Invalid Board")
        return -1
    if val is not 100 or -100 or 0.5 or -1:
        best = None
        for move in availableMoves(board):
                #print (availableMoves(board))
            new_board = makeMove(board, player, move)#new board
            #print(new_board)
            #print (minimax.nodes_explored)
            val = minimax(new_board, get_enemy(player))#new board
            if player == '1':
                if best is None or val > best:
                    best = val
            else:
                if best is None or val < best:
                    best = val
        return minimax.nodes_explored
    #return minimax.nodes_explored
minimax.nodes_explored = 0


#Question iii
#This function evaluates the board for winners or ties and returns the value
#it also perform alpha beta pruning to predict next best move for the provided
#player
def minimax_alphabeta(board, player,plies=1, alpha=-10000, beta=10000):
    val = staticEval(board)
    minimax.alphabeta_nodes_explored += 1
    if val == 100:
        print ("win for X")
        return 1
    #elif val == 0.5:
     #   print ("Tie")
      #  return 0.5
    elif val == -100:
        print ("win for O")
        return 0
 #   elif val == -1:
  #      return -1

    #print(minimax.alphabeta_nodes_explored)
    for move in availablePositions(board):
	p = get_enemy(player)
	if p == 1:
		board[move[0]][move[1]] = 1
	if p == 2:
		board[move[0]][move[1]] = 2 
	#     new_board = makeMove(board, player, move)
        #print (new_board)
        val = minimax_alphabeta(board, get_enemy(player),plies-1, alpha, beta)
	board[move[0]][move[1]] = 0
        if player =='2':
            if val > alpha:
                alpha = val
            if alpha >= beta:
                return beta
        else:
            if val < beta:
                beta = val
            if beta <= alpha:
                return alpha
    if player == '2':
        val = alpha
    else:
        val = beta
    return minimax.alphabeta_nodes_explored
    #print(minimax.alphabeta_nodes_explored)
minimax.alphabeta_nodes_explored = 0



#Question iv ---
#main function
def main():
#show(board)
    with open('temp.0') as f:
        board = [line.split() for line in f]

#    show(board)
    print ("minmax 'board1' has a win for Player '1' after exploring nodes: %s"  % str(minimax(board, player='1')))
    print ("alphabeta 'board1' has a win for player'1' after exploring nodes: %s"  % str(minimax_alphabeta(board, player='1', plies=6, alpha=-1000, beta=1000)))
    print ("--------------------------------------------------------------------------------")
    print(" ")
    show(board2)
    #print ("Evaluation of board 2: %s" %  str(evaluate_board(board2)))
    print ("minmax 'board2' has a win for player'1' after exploring nodes: %s"  % str(minimax(board2, player='1')))
    print ("alphabeta 'board2' has a win for player'1' after exploring nodes : %s"  % str(minimax_alphabeta(board2, player='1', plies=6, alpha=-1000, beta=1000)))
    print ("--------------------------------------------------------------------------------")
    print (" ")
    show(board3)
    #print ("Evaluation of board 3: %s" %  str(evaluate_board(board3)))
    print ("minmax 'board3' has a win for player'2' after exploring nodes: %s"  % str(minimax(board3, player='2')))
    print ("alphabeta 'board3' has a win for player'2' after exploring nodes : %s"  % str(minimax_alphabeta(board3, player='2', plies=6, alpha=-1000, beta=1000)))
    print ("--------------------------------------------------------------------------------")
main()
