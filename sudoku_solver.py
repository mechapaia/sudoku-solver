class Solution:
    def solveSudoku(self, board):
        self.solve(board)

    def solve(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':                  # finding empty positions in the board
                    for c in map(str, range(1, 10)):    # trying numbers from 1 to 9
                        if self.isValid(board, i, j, c):# checking if the board will be valid
                            board[i][j] = c
                            if self.solve(board):       # solving recursively
                                return True
                            board[i][j] = '.'           # resets the value
                    return False                        # no valid number found, backtrack
        return True                                     # returns solved sudoku board

    def isValid(self, board, row, col, c):
        for i in range(9):
            if (board[i][col] == c or                   # checking columns
                board[row][i] == c or                   # checking rows
                board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == c):       # checking the grid
                return False
        return True

# sample sudoku puzzle
board1 = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]



solver = Solution()
solver.solveSudoku(board1)

# printing the sudoku board
for row in board1:
    print(row)
print()

board2 = [
    [".",".",".",".",".",".",".",".","1"],
    [".",".",".",".",".",".",".","2","."],
    [".",".",".",".",".",".","3",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".","4",".",".",".","."],
    [".",".",".",".",".",".",".","5","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".","6",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."]
]
solver.solveSudoku(board2)

for row in board2:
    print(row)
print()


board3 = [
    [".",".",".",".",".","7",".",".","9"],
    [".","4",".",".","8","1","2",".","."],
    [".",".",".","6",".",".",".",".","."],
    [".",".",".",".",".",".","7",".","."],
    [".","1",".",".","2",".",".","9","."],
    [".",".","6",".",".",".",".",".","."],
    [".",".",".",".",".","2",".",".","."],
    [".",".","7","5","3",".",".","1","."],
    ["1",".",".","7",".",".",".",".","."]
]
solver.solveSudoku(board3)

for row in board3:
    print(row)
print()