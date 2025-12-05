"""
Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be 
played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in 
a draw return "Draw". If there are still movements to play return "Pending"."""

# time and space is o(9) -> o(1): since board size never changes: always at most 9

def tictactoe(self, moves: List[List[int]]) -> str:
    # a will play first
    # then b, and so on
    # create the board
    board = [[None for _ in range(3)] for _ in range(3)]
    players = ["A", "B"]

    for i, (r, c) in enumerate(moves):
        # A if odd, B if even
        board[r][c] = players[i % 2]
    print(board)

    # check all win conditions
    for i in range(3):
        # if board[i][0] is true and winning condition is met
        # get ith rows
            if board[i][0] and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        # get ith cols
            if board[0][i] and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    
    # get diagonal
    if board[0][0] and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    
    # get anti-diag
    if board[0][2] and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    
    # board is full, no wins
    if len(moves) == 9:
        return 'Draw'
    
    # board is incomplete, no wins yet
    if len(moves) < 9:
        return 'Pending'
