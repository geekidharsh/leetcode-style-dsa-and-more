"""
You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are within
the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in nums. Return the shortest sorted list 
of ranges that exactly covers all the missing numbers. That is, no element of nums is included in any of the ranges, and 
each missing number is covered by one of the ranges.
 
Example 1:
Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: [[2,2],[4,49],[51,74],[76,99]]
"""

def findmissingRanges(nums, lower, upper):
    result = []
    prev = lower - 1
    nums.append(upper + 1) # to cover final gap

    for num in nums:
        if num - prev > 1:
            rng = [prev + 1, num - 1]
            result.append(rng)
            # update prev to next possible range's start
        prev = num
    return result