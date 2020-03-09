"""
N-Queen problem using backtracking
"""

N = 4


# Function to print the solution
def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end="  ")
        print()


# A utility function to check if a queen is safe to be placed on the board[row][col]
# This function is called when "col" queens are already placed in columns form 0 to col-1
# so we have to check only left side for attacking queens
def isSafe(board, row, col):
    # check rows in the left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    # check the upper diagonal on left side
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # check the lower diagonal on left side
    for i, j in zip(range(row, N, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve(board, col):
    # Base case: If all queens are placed then return true
    if col >= N:
        return True

    # consider this row and try placing this queen in all rows one by one
    for i in range(N):
        if isSafe(board, i, col):
            # place this queen in board[i][col]
            board[i][col] = 1

            # recur to place the rest of the queens
            if solve(board, col + 1):
                return True

            # if placing queen in board[i][col] doesn't lead to
            # a solution, then remove the queen from the board[i][col]
            board[i][col] = 0

    # if the the queen can not be placed in any row
    # in this column then return false
    return False


def ans():
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0], ]
    if not solve(board, 0):
        print("Solution does not exists")
        return False
    printSolution(board)
    return True


if __name__ == '__main__':
    ans()
