"""You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.

Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.

 

Example 1:

Input: grid = [[1,3],[2,2]]
Output: [2,4]
Explanation: Number 2 is repeated and number 4 is missing so the answer is [2,4].
"""
# o(n^2) - time and space

def findMissingAndRepeat(grid):
    n = len(grid)
    freq_map = {}
    missing = None
    repeat = None
    # map for all possible numbers
    num_map = set(i for i in range(1, (n*n) + 1))
    # get freq_map and if a number repeats, update repeat
    for row in range(n):
        for col in range(n):
            num = grid[row][col]
            if num in freq_map:
                repeat = num
            else:
                freq_map[num] = 1
                num_map.remove(num)
    missing = num_map.pop() #remaining number is missing
    return [repeat, missing]