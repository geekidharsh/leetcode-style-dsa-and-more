# Maximum Subarray

# Given an integer array nums, find the contiguous subarray (containing at least one number) 
# which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

 
# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

nums = [-2,1,-3,4,-1,2,1,-5,4]

def maxSubarr(nums):
    current = nums[0]
    max_global = nums[0]
        
    if not nums:
        return max_global

    for i in range(len(nums)):
        current = max(nums[i], current + nums[i])
        max_global = max(max_global, current)
    return max_global


class Solution:
    def maxSubArrayPrefix(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        # approach is prefix sum approach
        # use float('inf') instead of 0, to make sure edge cases 
        # for negative values are handled
        min_sum = 0
        max_sum = float('-inf')
        prefix = 0
        for num in nums:
            prefix += num
            max_sum = max(max_sum, prefix - min_sum)
            min_sum = min(min_sum, prefix)
        
        return max_sum



print(maxSubarr(nums))