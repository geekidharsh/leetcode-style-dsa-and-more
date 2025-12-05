# Contains Duplicate

# Given an integer array nums, return true if any value appears at least twice 
# in the array, and return false if every element is distinct.


# ideal solution: o(n)

nums = [1,1,1,3,3,4,3,2,4,2]

# using hash tables
def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    count = {}
    for i in nums: 
        if i not in count:
            count[i] = 1
        else:
            return True
    return False

# using set
def containsDuplicateSet(nums):
    org = len(nums)
    unique = len(set(nums))
    return True if org > unique else False


print(containsDuplicate(nums))


# using sorting

# time: O(nlogn) (dominant by sorting operation which is o(nlogn)
# space: O(1)

def containsDupesSort(nums):
    l = len(nums)
    nums.sort()
    for i in range(l-1):
        if nums[i] == nums[i+1]:
            return True
    return False

print(containsDupesSort(nums))