# neetcode 150
# de shaw

# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) 
# connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid 
# are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island
# Return the maximum area of an island in grid. If there is no island, return 0.

# Input: 
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.

# time compexity: o(r * n)
# space: seen and areas (areas is optional) so o(n)
# recursive approach to walk through every 4 directions for each island
def maxAreaofIsland(grid):
    seen = set()
    row = len(grid)
    col = len(grid[0])

    def area(r, c):
        # if any of the below false then return area as 0 
        if not (0 <= r < row and 0 <= c < col and (r, c) not in seen and grid[r][c]):
                return 0
        # mark seen indices pairs as seen
        seen.add((r,c))
        # return 1 + new calculation
        return (1 + area(1+r, c) + area(r, c+1) + area(r-1, c) + area(r, c-1))

    areas = []
    for r in range(0, row):
        for c in range(0, col):
            areas.append(area(r, c))
    return max(areas)


print(maxAreaofIsland(grid))