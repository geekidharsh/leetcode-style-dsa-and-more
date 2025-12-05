# meta 100
# # Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
# Output: [4,2,6,5,7,1,3,9,8]

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.inorder(root, result)
        return result
    
    def inorder(self, root, result):
        if root is not None:
            self.inorder(root.left, result)
            result.append(root.val)
            self.inorder(root.right, result)


# iterative with stack
def inorderTraversal(self, root):
        res = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                # add node to stack
                stack.append(curr)
                # update node to left
                curr = curr.left
            # add latest stack value to result
            curr = stack.pop()
            res.append(curr.val)
            # update node to right
            curr = curr.right
        return res