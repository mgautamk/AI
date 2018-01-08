__author__ = 'student'

BOARD_SIZE = 8;

# weights = [[2885, 3391, 1494, 2404, 981, 1554, 2512, 3399],
#           [3208, 3417, 3243, 2684, 164, 1352, 2673, 1206],
#           [450, 559, 2806, 2632, 344, 2711, 978, 2073],
#           [3235, 3437, 3398, 1389, 2916, 2816, 2407, 793],
#           [2240, 3390, 2322, 2322, 2461, 662, 2320, 2661],
#           [346, 1719, 127, 607, 1123, 1735, 576, 904],
#           [987, 2834, 3007, 2501, 3365, 1578, 422, 1792],
#           [1937, 503, 3308, 113, 122, 2289, 1765, 2476]]

weights = [[ 4693,       4289,        1853,        2004,        2996,         873,        1207,         562],
        [5053,        1283,       4376,        2991,        2473,        3171,        4811,        5067],
        [2883,        4895,        3083,         400,          63,        1386,         803,          25],
        [ 731,        1844 ,       2896,         285,        1776,        3446,        4350,        4082],
         [787,        1036,        4831,        2796,         855,        3631,        2836,        4305],
        [1357,        1323,        1506,        4104,        4184,        3941,        5247,        4576],
        [4429,        3245,        3989,        4920,        1640,        2374,         412,         445],
        [1340,        2493,        3970,         685,        2784,         442,        2332,        2106 ]]


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
    smaller_solutions = solve(n-1, weight) # Recursion
    solutions = []

    for solution in smaller_solutions: #for loop
        for column in range(1,BOARD_SIZE+1):
        #add a new queen to the row or atleast try
            if not under_attack(column, solution):
                solutions.append(solution + [(n, column)])

    return solutions



lowest_weight = float('inf')
best_route = [[]]
for answer in solve(BOARD_SIZE, 0):
    weight = 0
    for point in answer:
        weight += weights[point[0] - 1][point[1] - 1]
    if weight < lowest_weight :
        lowest_weight = weight
        best_route = answer


print("Uniform Cost Serach:",best_route, "cost:", lowest_weight)
