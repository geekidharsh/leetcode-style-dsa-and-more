# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,1]
# Output: 1

nums = [2,2,1]

from collections import Counter
def singleNumber(nums):
    num_map = Counter(nums)
    for key, val in num_map.items():
        if val == 1:
            return key
 

singleNumber(nums)