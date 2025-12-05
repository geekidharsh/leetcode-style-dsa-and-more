# Diameter of Binary Tree

# Given the root of a binary tree, return the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any 
# two nodes in a tree.  This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.


# solution: 
    # key observation: diameter of the tree is determined by the sum of the two longest paths from any node's left and right subtrees
    # so we get longest sum of left + right path recursively
    # keep replacing it with max so far
    # return max
    # dfs is needed, using a helper function is key

def diameterOfBinaryTree(self, root) -> int:
    self.diameter = 0  # To store the maximum diameter

    # use helper dfs to get height
    def dfs(curr):
        # base case            
        if not curr:
            return 0
        left = dfs(curr.left)
        right = dfs(curr.right)
        # this is the tricky part to memorize
        self.diameter = max(self.diameter, left + right)
        return 1 + max(left, right)
        
    dfs(root)
    return self.diameter



