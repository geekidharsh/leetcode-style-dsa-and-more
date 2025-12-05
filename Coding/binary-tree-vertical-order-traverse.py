# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# meta 100

from heapq import *
from collections import defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # imagine looking at the tree from the top
        # now traverse it left to right
        # we need to get values left to right (sorting by x) and within same x -> top to bottom (sorting by y) 
        # imagine two axis x and y for this question
        # to get values top to bottom (while going left to right), we will use dfs and grouping
        # start from root, for left to x-1, for right x+1 to keep track of positions

        # create a group of x values: for each x -> store y location of value + value
        result_x = defaultdict(list) #group values by x-axis: x: (y-axis, node.val)

        if not root:
            return []

        def dfs(curr, x, y):
            if not curr: 
                return
            result_x[x].append((-y, curr.val))
            dfs(curr.left, x-1, y-1)
            dfs(curr.right, x+1, y-1)

        dfs(root, 0, 0)

        # now sort to get values left to right
        output = []
        
        for key, val in sorted(result_x.items()):
            temp = []
            while val:
                candidate = heappop(val)
                temp.append(candidate[1])
            output.append(temp)
        return output