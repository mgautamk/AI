#/usr/bin/python
#Mahesh Gutam

BOARD_SIZE = 8;

def under_attack(column, existing_queens):
    # ASSUMES that row = len(existing_queens) + 1
    row = len(existing_queens)+1
    for queen in existing_queens:
        r,c = queen
        if r == row: return True # Check row
        if c == column: return True # Check column
        if (column-c) == (row-r): return True # Check left diagonal
        if (column-c) == -(row-r): return True # Check right diagonal
    return False

def solve(n):
    if n == 0: return [[]] # no recursion if n = 0
    smaller_solutions = solve(n-1) # Recursion bitch
    solutions = []
    for solution in smaller_solutions: #for loop biatch
        for column in range(1,BOARD_SIZE+1):
        #add a new queen to the row or atleast try
            if not under_attack(column, solution):
                solutions.append(solution + [(n, column)])
    return solutions

#print them
i = 0
for answer in solve(BOARD_SIZE): 
    print answer
    i = i + 1
print i
