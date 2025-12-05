# Given an integer array nums with possible duplicates, randomly output the index of a given target number. 
# You can assume that the given target number must exist in the array.

# Implement the Solution class:

# Solution(int[] nums) Initializes the object with the array nums.
# int pick(int target) Picks a random index i from nums where nums[i] == target. 
# If there are multiple valid i's, then each index should have an equal probability of returning.
 

# Example 1:
# Input
# ["Solution", "pick", "pick", "pick"]
# [[[1, 2, 3, 3, 3]], [3], [1], [3]]
# Output
# [null, 4, 0, 2]


class Solution:

    def __init__(self, nums: List[int]):
        # get num map of number and their indices, use it for looking all places where a number is
        self.num_map = {}
        for idx, num in enumerate(nums):
            if num not in self.num_map:
                self.num_map[num] = [idx]
            else:
                self.num_map[num].append(idx)            

    def pick(self, target: int) -> int:
        # since target will always be in nums, look up target in num_map
        # get all indices that are stored as a list in num_map for that target num
        # now randomly pick one of these indices
        # return indices[rand_idx]

        indices = self.num_map[target]
        rand_idx = randint(0, len(indices) - 1)
        return indices[rand_idx]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)