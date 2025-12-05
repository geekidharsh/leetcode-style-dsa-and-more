"""
Graph and dfs question
samsung, meta, google, bloomberg, linkedin, apple

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

"""
class Solution:
    def numIslands(self, matrix: List[List[str]]) -> int:
        # approach
        # need is to find 1s and all neighbors that are 1s
        # recursively looking left right top bottom
        # keep a set of all visited points in the matrix
        # trick is to get all edge cases for dfs right:
        # r or c should not be out of bounds 
        def dfs(r, c): #helper dfs
            # base case
            if r >= row or c >= col or r < 0 or c < 0 or matrix[r][c] == '0' or (r,c) in visited:
                return
            visited.add((r,c))
            
            # go down, left, up, right
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)

        
        islands = 0
        visited = set()
        row = len(matrix)
        col = len(matrix[0])

        for r in range(row):
            for c in range(col):
                if matrix[r][c] == '1' and (r, c) not in visited:
                    # found a brand new island.
                    # Now explore and mark all its land
                    dfs(r, c)
                    islands += 1
            print(visited)

        return islands
