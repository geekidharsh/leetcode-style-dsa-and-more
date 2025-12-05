# You are given a 0-indexed array nums of size n consisting of non-negative integers.
# If nums[i] == nums[i + 1], then multiply nums[i] by 2 and set nums[i + 1] to 0. Otherwise, you skip this operation.
# lastly, shift all the 0's to the end of the array.
# For example, the array [1,0,2,0,0,1] after shifting all its 0's to the end, is [1,2,1,0,0,0].

# nums = [1,2,2,1,1,0]
# Output: [1,4,2,0,0,0]

# solution: 
# o(n) + o(nlogn) -> o(nlogn), space: o(1)

def applyOperationToArr(nums):
    # easy to get this part
    for i in range(len(nums)-1):
        if nums[i] != 0 and nums[i] == nums[i+1]:
            temp = 2 * nums[i]
            nums[i] = temp
            nums[i + 1] = 0

    # now sort by key 0
    # The function lambda x: x == 0 returns: True (or 1) if x is 0, and False(or 0) for any non zero element
    # since, False(0) comes before True(1) in boolean,
    # this arranges all non zero items before zero
    nums.sort(key=lambda x: x == 0)
    return nums
