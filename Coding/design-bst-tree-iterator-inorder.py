"""
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the 
constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns 
false. int next() Moves the pointer to the right, then returns the number at the pointer.

example: 
Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# approach:
    # bst takes in order: left -> root -> right. So to maintain order of values iteratively, we use a stack
    # a helper function inorderTraverseLeft(self, node), used to get all left nodes
    # next will look at the top value from the stack and return it, while checking if right child exists
    # if right child exists, call helper function to stack all it's left children nodes

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.inorderTraverseLeft(root)
    
    def inorderTraverseLeft(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        # perform an in - order traversal
        # left subtree → current node → right subtree
        top_node = self.stack.pop()
        if top_node.right:
            # if top node has right child, get all left nodes of the child
            self.inorderTraverseLeft(top_node.right)
        return top_node.val

    def hasNext(self) -> bool:
        if len(self.stack):
            return True
        else:
            return False
