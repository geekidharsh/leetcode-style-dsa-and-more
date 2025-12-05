# two sum / 2sum

# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    required = {}
    for i in range(len(nums)):
        if (target - nums[i]) in required:
            return [i, required[target - nums[i]]]
        else:
            required[nums[i]] = i

nums = [2,7,11,15]
target = 11

p = twoSum(nums, target)
print(p)
