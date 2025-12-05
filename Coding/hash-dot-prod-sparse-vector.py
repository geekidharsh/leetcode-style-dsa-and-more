# Dot Product of Two Sparse Vectors

# Implement class SparseVector:
# SparseVector(nums) Initializes the object with the vector nums
# dotProduct(vec) Compute the dot product between the instance of SparseVector and vec

class SparseVector:
    def __init__(self, nums: List[int]):
        # storing indices with values that are non zero
        self.s_vec = {}
        for idx, val in enumerate(nums):
            if val != 0:
                self.s_vec[idx] = val

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        # iterating through incoming SparseVector val and checking if item at same index,
        # then get result
        for i, val in vec.s_vec.items():
            if i in self.s_vec:
                ans += val * self.s_vec[i]
        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

# Input: 
nums1 = [1,0,0,2,3]
nums2 = [0,3,0,4,0]
# Output: 8