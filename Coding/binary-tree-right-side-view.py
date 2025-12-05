"""
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Input: 
root = [1,2,3,4,null,null,null,5]
            1
        2       3
    4
5
Output: 
[1,3,4,5] (as seen from right)
"""
# approach: 
# dfs approach with going right first
# check all right nodes and keep storing values along with depth
# once, all right has been exhausted, now keep checking for left nodes at
# last right node's depth and deeper

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    # get node val as seen from right side
    right_side = []

    def dfs(node, depth):
        if not node:
            return

        # first node only, at each depth
        # since we go right first, this ensures - record first right at the curr depth
        # starting from depth 0
        if depth == len(right_side):
            right_side.append(node.val)
        
        # go right first 
        dfs(node.right, depth + 1)
        # all right has been exhausted, now keep checking for left nodes at
        # last right node's depth and deeper
        dfs(node.left, depth + 1)
    
    dfs(root, 0)
    return right_side