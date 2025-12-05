# topic: array, matrix, backtrack algo

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or 
# vertically neighboring. The same letter cell may not be used more than once.

# Input: 
# board = [["A","B","C","E"],
#          ["S","F","C","S"],
#          ["A","D","E","E"]]
# word = "ABCCED"
# Output: true

# intuition:
    # not an easy one but understanding backtrack algo helps greatly.
    # use backtrack
    # 1. here we need to explore each cell in the word grid
    # 2. if the letter in word matches, we start a dfs
    # 3. dfs will check all it's neighbors and if next word is match, repeat 2
    # 4. if any dfs returns the word, return True
    # 5. keep marking visited cell, to avoid reusing

board1 = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word1 = "ABCCED"

def word_search(board, word):
    visited = set()
    rows = len(board)
    col = len(board[0])
    
    def dfs(i, j, pos):
        
        if pos == len(word): # entire word is explored in grid, so return true
            return True
        
        # Check boundaries and if the current cell doesn't match
        if i < 0 or i >= rows or j < 0 or j >= col or (i, j) in visited or board[i][j] != word[pos]:
            return False
        
        # temporarily mark cells as visited
        visited.add((i, j))
        
        # Explore all 4 directions: down, up, right, left.
        found = (dfs(i + 1, j, pos + 1) or
                 dfs(i - 1, j, pos + 1) or
                 dfs(i, j + 1, pos + 1) or
                 dfs(i, j - 1, pos + 1))
        
        # remove cells from visited since we are backtracking
        visited.remove((i, j))
        return found
        
    
    # explore every char in word grid
    for rw in range(rows):
        for cl in range(col):
            # if char is in word
            if board[rw][cl] == word[0]:
                # launch recursive calls
                if dfs(rw, cl, 0):
                    return True
    return False

# test code
print('testing...')
assert word_search(board=board1, word=word1) == True
assert word_search(board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word="ABCB") == False
print('test passed. Done')