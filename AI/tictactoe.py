#!/usr/bin/python
#----------------------------------------------------------------------------
#Author: Mahesh Gautam
#Class: CS 480 AI
#Instructor: Dr. Bala RaviKumar
#Assignment: Midterm 1 
#Description: Implementation of Minmax algorithm and Alpha beta pruning 
# on Tic Tac Toe two player game where player wins if they have no boxes 
#with same Xs or Os in same row or column 
#------------------------------------------------------------------------------
import sys
import random 
import getopt

board = [
    ["O", "X", "X", "-"],
    ["X", "X", "O", "-"],
    ["O", "-", "X", "O"],
    ["X", "O", "O", "-"]]

#print the board in Tic Tac toe fashion
def show():
    print board[0][0], '|' , board[0][1], '|' ,board[0][2], '|' ,board[0][3]
    print '--------------'
    print board[1][0], '|' , board[1][1], '|' ,board[1][2], '|' ,board[1][3]
    print '--------------'
    print board[2][0], '|' , board[2][1], '|' ,board[2][2], '|' ,board[2][3]
    print '--------------'
    print board[3][0], '|' , board[3][1], '|' ,board[3][2], '|' ,board[3][3]

#Winning combinations
winning_combos = [
    [0, 5, 10, 15]]

#Is Complete
def isComplete(board):
    return true

#Global variables         
x_rows = [] #x rows
x_cols = [] #x columns
o_rows = [] #o rows
o_cols = [] #o columns 

#This function returns score 0 for win of 0, 1 for win of X, -1 for invalid board and 0.5 for tie
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
                if col == 'X':
                    x_count += 1
                    if row_index not in x_rows:
                        x_rows.append(row_index)
                    if col_index not in x_cols:
                        x_cols.append(col_index)
                elif col == 'O':
                    o_count += 1
                    if row_index not in o_rows:
                        o_rows.append(row_index)
                    if col_index not in o_cols:
                        o_cols.append(col_index)
                col_index += 1
            row_index += 1
        if len(x_rows) == 4 and len(x_cols) == 4: #Is complete for x 
            x_win = True
        if len(o_rows) == 4 and len(o_cols) == 4: # IS complete for 0 
            o_win = True
    except Exception as e:
        print e
        return -1
    if o_count != x_count and o_count - 1 != x_count:
        print "counts %s %s" % (str(x_count), str(o_count))
        return -1
    if x_win:
        if o_win:
            return 0.5
        else:
            return 0
    elif o_win:
        return 0
    else:
        return -2

def get_move(board):
    val = evaluate_board(board)
    if val == -2:
        x_missing_rows = []
        x_missing_cols = []
        o_missing_rows = []
        o_missing_cols = []
        x_candidate = []
        o_candidate = []
        for i in (0,3):
            if i not in x_rows:
                x_missing_rows.append(i)
            if i not in x_rows:
                x_missing_rows.append(i)
            if i not in o_cols:
                o_missing_cols.append(i)
            if i not in o_cols:        
                o_missing_cols.append(i)
        for i in x_missing_rows:
            for j in x_missing_cols:
                if board[i][j] == '-':
                    x_candidate.append([i, j])
        for i in o_missing_rows:
            for j in o_missing_cols:
                if board[i][j] == '-':
                    o_candidate.append([i, j])
        if len(x_candidate) == 0 and len(o_candidate) == 0:
            # draw
            return 0.5
        return x_candidate
            
    else:
        return val

#show(board)

show()
print "result %s" % str(get_move(board))
