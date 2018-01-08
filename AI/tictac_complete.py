import random

def makeMove(board, player, location):
    gridlist = list(board)
    gridlist[location] = player
    return ''.join(gridlist)

def printBoard(board):

    print ' ' + ' | '.join(board[0:3])
    print '-'*10
    print ' ' + ' | '.join(board[3:6])
    print '-'*10
    print ' ' + ' | '.join(board[6:9])
    print '_'*12



def winner(board):
    for row in winning_combos:
        if (board[row[0]] != ' ') and (equal([board[i] for i in row])):
            return board[row[0]]

def equal(row):
    return row == [row[0]] * 3

winning_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]]

def availableMoves(board):
    return [k for k, v in enumerate(board) if v == ' ']

def isComplete(board):
    if winner(board):
        return True
    return availableMoves(board) == []

def x_won(board):
    return winner(board) == 'x'

def o_won(board):
    return winner(board) == 'o'

def tied(board):
    return isComplete(board) and winner(board) is None

def get_enemy(player):
    if player == 'x':
        return 'o'
    else:
        return 'x'

def score(board):
    if x_won(board):
        return -1
    elif o_won(board):
        return 1
    elif tied(board):
        return 0

def minimax(board, player):
    if isComplete(board):
        return score(board)
    best = None
    for move in availableMoves(board):
        new_board = makeMove(board, player, move)
        val = minimax(new_board, get_enemy(player))
        if player == 'o':
            if best is None or val > best:
                best = val
        else:
            if best is None or val < best:
                best = val
    return best

def determine(board, player):
    a = -2
    choices = []
    for move in availableMoves(board):
        new_board = makeMove(board, player, move)
        val = minimax(new_board, get_enemy(player))
        if player == 'o':
            if val > a:
                a = val
                choices = [move]
            elif val == a:
                choices.append(move)
    return random.choice(choices)

def get_input(board):
    move = input('Make a move for x:') 
    if move not in availableMoves(board):
        print 'Illegal Move - Already Taken. Choose again!'
        get_input(board)
    else:
        return move
    

welcome_mes = '''Welcome to Tic Tac Toe against the AI!
0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8
There's the board, make your move!
'''


######################################
##########Main Game Class#############
######################################

class Game(object):
    def __init__(self, grid=''):
        if grid:
            self.grid = grid
        else:
            self.grid = ' '*9

        self._currentTurn = 'x'

    def swapTurn(self):
        if self._currentTurn == 'x':
            self._currentTurn = 'o'
        else:
            self._currentTurn = 'x'

    def start(self):
        print welcome_mes
        printBoard(self.grid)
        while not isComplete(self.grid):
            if self._currentTurn == 'x':
                try:
                    move = get_input(self.grid)
                except:
                    print 'Not a legal move. Try again?'
                    move = get_input(self.grid)
                self.grid = makeMove(self.grid, self._currentTurn, move)
            elif self._currentTurn == 'o':
                self.grid = makeMove(self.grid, self._currentTurn, determine(self.grid, self._currentTurn))
            self.swapTurn()
            printBoard(self.grid)
        if winner(self.grid): 
            print winner(self.grid) + ' is the winner!'
        else:
            print 'Tie game!'

def main():
    game = Game()
    game.start()

if __name__ == '__main__':
    main()
