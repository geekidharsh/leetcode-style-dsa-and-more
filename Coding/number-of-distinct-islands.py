"""
follow up of number of island. 
You are given an m x n binary matrix grid. An island is a group
An island is considered to be the same as another if and only if one island can be translated
(and not rotated or reflected) to equal the other.
Return the number of distinct islands.
Input: 
grid = [[1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,0,1,1],
        [0,0,0,1,1]]
Output: 1 (top left and top right are similar so distinct is only 1)
"""

class Solution:
    def numDistinctIslands(self, matrix) -> int:
        """
        approach:
        similar to number of island - do that first
        uses DFS to explore each island and records its shape as a list
        of relative coordinates from the origin of that island."""        
        def dfs(r, c, origin_r, origin_c, shape):
            if r < 0 or c < 0 or r >= row or c >= col:
                return
            if matrix[r][c] == 0 or (r,c) in visited:
                return
            visited.add((r,c))
            # record shape relative to the origin
            shape.append((r - origin_r, c - origin_c))

            dfs(r+1, c, origin_r, origin_c, shape)
            dfs(r-1, c, origin_r, origin_c, shape)
            dfs(r, c+1, origin_r, origin_c, shape)
            dfs(r, c-1, origin_r, origin_c, shape)
            # -------
            
        visited = set()
        row = len(matrix)
        col = len(matrix[0])
        distinct_shapes = set()

        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 1 and (r,c) not in visited:
                    shape = []
                    dfs(r,c, r, c, shape)
                    print(shape)
                    distinct_shapes.add(tuple(shape))
        # print(distinct_shapes)
        return len(distinct_shapes)
