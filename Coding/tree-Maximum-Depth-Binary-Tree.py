# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down 
# to the farthest leaf node.

# solution:
    # if root is null then depth is 0
    # otherwise, depth is at least 1. i.e -> root + max(left, right)
    # since depth is needed, we can do dfs
    # O(H)
    
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def maxDepth(root):
    if not root:
        return 0

    count_left = maxDepth(root.left)
    count_right = maxDepth(root.right)
    
    return 1 + max(count_left, count_right)
    