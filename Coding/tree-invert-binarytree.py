# Given the root of a binary tree, invert the tree, and return its root.

# Input: root = [2,1,3]
# Output: [2,3,1]
# so all left nodes become right and right becomes left


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# example
# root = TreeNode()
# add value and left, right nodes

def invertBinaryTree(root):
    if not root:
        return
    
    # recursively get left and right in memory
    left = invertBinaryTree(root.left)
    right = invertBinaryTree(root.right)
    
    # now invert
    root.left = right
    root.right = left
    
    return root
    