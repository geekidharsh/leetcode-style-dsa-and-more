# Given the root node of a binary search tree and two integers low and high, 
# return the sum of values of all nodes with a value in the inclusive range [low, high].
# example: root = [10,5,15,3,7,null,18], low = 7, high = 15
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# intuition:
    # straight forward problem
    # get dfs to recursively touch all nodes
    # if a node is in the range, add it to result
    # time: o(n)
    # space: o(h) - each recursive call is stored in memory. max depth is H (avg case), 
    # best is O(logN) in balanced tree

class Solution:
    def bstRangeSum(self, root, low, high):
        self.result = 0
        # optional use of set(), to improve time. Uses extra space
        self.visited = set()

        def dfs(node):
            if not node:
                return
            # iterate over all values in the range, inclusive
            if low <= node.val <= high and node not in self.visited:
                self.visited.add(node)
                self.result += node.val
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.result