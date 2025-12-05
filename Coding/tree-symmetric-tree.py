"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center). Get mirror image

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
101. Symmetric Tree

linkedin, google, amazon, bloomberg    """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # o(n), use tree twice in a helper function, iterate dfs style: left and right
        
            return self.helper(root, root)
    
    def helper(self, t1, t2):
        # base case
        if t1 is None and t2 is None:
            return True
        # if either one is None but not the other
        if t1 is None or t2 is None:
            return False
        
        if t1.val == t2.val:
            return self.helper(t1.right, t2.left) and self.helper(t1.left, t2.right)
        else:
            return False