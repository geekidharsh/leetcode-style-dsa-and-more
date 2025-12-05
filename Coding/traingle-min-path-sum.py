# de shaw
# 120. Triangle

# Given a triangle array, return the minimum path sum from top to bottom.

# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, 
# you may move to either index i or index i + 1 on the next row.

#  Example 1:

# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).


triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]

def triangleMinPathSum(triangle):
    """
    get minimum path sum of a triangle represented in an array
    """
    dp = [0] * (len(triangle) + 1)
    for row in triangle[::-1]:
        # go from the bottom to top using python reverse walk, dfs like approach 
        for i, num in enumerate(row):
            # for each index i and number num, look at the adjacent items above and get min 
            dp[i] =  num  + min(dp[i], dp[i+1])
    print(dp)

    return dp[0]


triangleMinPathSum(triangle)