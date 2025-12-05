# nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# find all triplet that sum to zero
# Notice that the solution set must not contain duplicate triplets.


nums = [-1,0,1,2,-1,-4]

def threeSum(nums):
    # approach
    # since order of items not important in result
    # we sort the values
    # start from left and right pointers, sum and compare
    # time: o(n^2) optimal for 3sum
    # space: o(n) - cos of set
    result = set()         # use of set to avoid duplicate triplets
    nums.sort()
    for i in range(len(nums)):
        # skip duplicate anchor i's
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        target = - nums[i]
        left = i + 1
        right = len(nums) - 1
        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum == target:
                result.add((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1

            elif curr_sum < target:
                left += 1
            else:
                right -= 1
    return list(result)


threeSum(nums)