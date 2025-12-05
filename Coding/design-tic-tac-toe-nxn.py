"""
Rules:
A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves are allowed.
Implement the TicTacToe class:

TicTacToe(int n) Initializes the object the size of the board n.
int move(int row, int col, int player) Indicates that the player with id player plays at the cell (row, col) 
of the board. The move is guaranteed to be a valid move, and the two players alternate in making moves. 
Return
0 if there is no winner after the move,
1 if player 1 is the winner after the move, or
2 if player 2 is the winner after the move.

Input
["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
[[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
Output
[null, 0, 0, 0, 0, 0, 0, 1]
"""

class TicTacToe:

    def __init__(self, n: int):
        # take n
        # for every player update row, col and diag / anti-diag
        # When a move is made:
        # The respective row, column, and diagonals are updated for the player.
        # If any of them reaches n, the player wins.
        # Otherwise, the game continues with no winner (0 is returned).

        self.n = n
        self.r = [0] * n
        self.c = [0] * n
        self.diag = [0, 0]
        
    def move(self, row: int, col: int, player: int) -> int:
        score = 1 if player == 1 else -1 
        
        # mark player on the board
        self.r[row] += score
        self.c[col] += score
        # print(self.r, self.c)

        # if row and col same, update diag[0] (left to right)
        if row == col:
            self.diag[0] += score
        # update anti diag, (right to left)
        if row + col == self.n - 1:
            # anti-diag
            self.diag[1] += score
        # * is to unpack diag in below
        # need to understand this more - below 
        for s in (self.r[row], self.c[col], *self.diag):
            if abs(s) == self.n:
                return 1 if s > 0 else 2
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)