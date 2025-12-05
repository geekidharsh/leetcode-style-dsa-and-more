"""
Graph traversal problem that involves shortest path finding with a state constraint — specifically, 
a limited number of "lives" or resources 
This falls under the category of:
- Shortest Path in Grid with Constraints
- BFS with State Tracking
- Multi-dimensional BFS (you track more than just coordinates)
- a Modified Dijkstra if weights are involved

**Problem:**
Given a 2D grid `maze` representing a maze, where:
* `0` = Empty space (walkable)
* `1` = Wall (impassable)
* `6` = Monster (walkable, but consumes 1 life)

A character starts at `(si, sj)` and aims to reach `(ei, ej)`. The character has `N` lives. 
Find the shortest path from the start to the end, considering the character can walk over at most 
`N-1` monsters.

**Constraints:**
* Movement is restricted to the 4 cardinal directions (up, down, left, right).
* Return `-1` if no path exists.

**Example:**

input:
maze = [
    [0, 0, 1, 0],
    [6, 0, 0, 0],
    [0, 1, 6, 0],
    [0, 0, 0, 0]
]
si, sj = 0, 0
ei, ej = 3, 3
N = 2

print(shortest_path_with_monsters(maze, si, sj, ei, ej, N))  # Output: 7

"""
maze = [
    [0, 0, 1, 0],
    [6, 0, 0, 0],
    [0, 1, 6, 0],
    [0, 0, 0, 0]
]
si, sj = 0, 0
ei, ej = 3, 3
N = 2

def shortest_path_with_monsters(maze, si, sj, ei, ej, N)):
    row = len(maze)
    col = len(maze[0])
    max_potential_monsters = N - 1
    