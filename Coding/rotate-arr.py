# meta 100
# # Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Given an integer array nums, rotate the array to the right by k steps, 
# where k is non-negative.

nums = [1,2,3,4,5,6,7]
k = 3

def rotateArr(nums, k):
    # this solution does not modify in place
    # reverse all elements to bring last to the front
    nums.reverse()

    # reverse first k elements
    first_k_elem = nums[:k]
    first_k_elem.reverse()
    
    # reverse n-k elems
    remaining_elem = nums[k:]
    remaining_elem.reverse()
    
    # join both to get result
    result = first_k_elem + remaining_elem
    nums = result
    return nums



def rotateArrInPlace(nums, k):
    # reverse all elem in arr to bring back to front
    nums.reverse()
    # print(nums)
    
    n = len(nums)
    nums[:k] = reversed(nums[:k])
    print(nums)
    nums[k:] = reversed(nums[k:])
    print(nums)
     


# rotateArr(nums, k)
rotateArrInPlace(nums, k)

