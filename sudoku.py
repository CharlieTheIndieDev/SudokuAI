#This is the solver where we input the board inside code and it solves the board using backtracking. 
#each time the code backtracks we print the backtrack statement and finally print out the final solution.
#Has been tested for the easiest to the hardest sudoku puzzles including Escargot's Sudoku puzzle board
#=========================================================================================================

#Easy board
# board = [
#     [7,8,0,4,0,0,1,2,0],
#     [6,0,0,0,7,5,0,0,9],
#     [0,0,0,6,0,1,0,7,8],
#     [0,0,7,0,4,0,2,6,0],
#     [0,0,1,0,5,0,9,3,0],
#     [9,0,4,0,6,0,0,0,5],
#     [0,7,0,3,0,0,0,1,2],
#     [1,2,0,0,0,7,4,0,0],
#     [0,4,9,2,0,6,0,0,7]
# ]

#unsolvable board
# board = [
# 		[0, 0, 0, 0, 0, 0, 0,0, 1],
#         [0, 0, 0, 0, 0, 2, 0, 3, 0],
#         [0, 0, 0, 0, 3, 0, 4, 2, 0],
#         [0, 0, 4, 0, 0, 0, 5, 6, 0],
#         [0, 0, 6, 3, 0, 4, 0, 0, 0],
#         [0, 1, 0, 8, 0, 0, 0, 0, 0],
#         [0, 0, 5, 0, 0, 6, 3, 0, 0],
#         [0, 8, 0, 7, 0, 0, 0, 0, 9],
#         [9, 0, 0, 1, 0, 0, 0, 0, 0]
# ]

# =============================================================================
#test board (difficult)
# board = [
#     [8, 0, 0, 0, 0, 0, 0,0, 0],
#     [0, 0, 3, 6, 0, 0, 0, 0, 0],
#     [0, 7, 0, 0, 9, 0, 2, 0, 0],
#     [0, 5, 0, 0, 0, 7, 0, 0, 0],
#     [0, 0, 0, 0, 4, 5, 7, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0, 3, 0],
#     [0, 0, 1, 0, 0, 0, 0, 6, 8],
#     [0, 0, 8, 5, 0, 0, 0, 1, 0],
#     [0, 9, 0, 0, 0, 0, 4, 0, 0]
# ]
# =============================================================================

#Escargot's Sudoku board
board = [
    [1, 0, 0, 0, 0, 7, 0,9, 0],
    [0, 3, 0, 0, 2, 0, 0, 0, 8],
    [0, 0, 9, 6, 0, 0, 5, 0, 0],
    [0, 0, 5, 3, 0, 0, 9, 0, 0],
    [0, 1, 0, 0, 8, 0, 0, 0, 2],
    [6, 0, 0, 0, 0, 4, 0, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 4, 1, 0, 0, 0, 0, 0, 7],
    [0, 0, 7, 0, 0, 0, 3, 0, 0]
]

#print_board(board)
def solve(bo):
    print(" ")
    print(bo)
    print(" ")
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
               return True

            bo[row][col] = 0
            print("Backtrack")

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

print("Original Board")
print_board(board)
solve(board)
print(" ")
print("The solution is: ")
print("___________________")
print(" ")
print_board(board)
