#/usr/bin/python
#Mahesh Gutam

BOARD_SIZE = 8;

weights = [[2885, 3391, 1494, 2404, 981, 1554, 2512, 3399],
          [3208, 3417, 3243, 2684, 164, 1352, 2673, 1206],
          [450, 559, 2806, 2632, 344, 2711, 978, 2073],
          [3235, 3437, 3398, 1389, 2916, 2816, 2407, 793],
          [2240, 3390, 2322, 2322, 2461, 662, 2320, 2661],
          [346, 1719, 127, 607, 1123, 1735, 576, 904],
          [987, 2834, 3007, 2501, 3365, 1578, 422, 1792],
          [1937, 503, 3308, 113, 122, 2289, 1765, 2476]]

cost = [8]

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

def solve(n, weight):
    if n == 0: return [[]] # no recursion if n = 0
    smaller_solutions = solve(n-1, weight) # Recursion bitch
    solutions = []
    
    for solution in smaller_solutions: #for loop biatch
        for column in range(1,BOARD_SIZE+1):
        #add a new queen to the row or atleast try
            if not under_attack(column, solution):
                weight += weights[n-1][column -1]
                print (n, column, weights[n-1][column-1])
                print "\n"
                solutions.append(solution + [(n, column)])
    return solutions

#print them
i = 0
for answer in solve(BOARD_SIZE, 0): 
    #print answer
    i = i + 1
print i
