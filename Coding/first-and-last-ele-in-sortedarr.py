# Given an array of integers nums sorted in non-decreasing order, find the starting and ending 
# position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.


# approach:
# since it's sorted, let's think of a binary search approach
# look for the target
# once target is found, using start and end position, traverse both ways until target equal nums[i] position

# Input: 
nums = [5,7,7,8,8,10]
target = 8
# Output: [3,4]

def searchRange(nums, target):
    if not nums:
        return [-1, -1]
    start = 0
    end = len(nums) - 1
    # find target value in nums using binary search
    while start <= end:
        mid = (start + end)// 2
        if nums[mid] == target:
            start = end = mid
            # print(nums[mid], start, end)
            # now we need to find the start and end position of target
            while start > 0 and nums[start - 1] == target:
                start -= 1
            while end < len(nums) - 1 and nums[end + 1] == target:
                end += 1
            return [start, end]
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return [-1, -1]

searchRange(nums, target)