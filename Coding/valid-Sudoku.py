"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated
according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the 
digits 1-9 without repetition.


inp = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

"""
# Solution explained: 
# - This question only asks to validate filled values in sudoku. 
#     - This means only filled values need to be validated for duplicates.
#     - solution then is merely - iterating over all rows and columns and then determining any duplicates found per row and column.
#     - we also need to do duplication check for each of the 3x3 boxes.
#     - overall solution can be desgined using a hashmap - per row and column. 
#     - I am using a set() comparison which is same as using hash operations: o(1)
#     - time: o(n^2)
#     - space: o(n) or n-squared (not sure)



inp = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


def isValidSudoku(board):
    N = 9
    
    # for all rows
    for r in range(N):
        row = [r_item for r_item in board[r] if r_item != '.']
        if len(row) != len(set(row)):
            return False

    # for all columns
    for c in range(N):
        column = [board[r][c] for r in range(N) if board[r][c] != '.']
        if len(column) != len(set(column)):
            return False

    def helper(R,C):
        # helper function for the subboxes of 3by3 size
        l = set()
        for r in range(R, R+3):
            for c in range(C, C+3):
                if board[r][c] == '.': continue
                if board[r][c] not in l:
                    l.add(board[r][c])
                else:
                    return False
        return True
    
    # using the helper function for each 3x3 box: starting from 0,3
    for r in range(0,N,3):
        for c in range(0,N,3):
            if not helper(r,c):
                return False
    
    return True


print(isValidSudoku(inp))
