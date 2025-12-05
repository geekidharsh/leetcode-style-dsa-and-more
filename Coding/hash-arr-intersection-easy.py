# - given two arr, return their intersection
# result must be unique values only and can be returned in any order

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.

def arrIntersection(nums1, nums2):
    num1_set = set(nums1)
    num2_set = set(nums2)
    
    result = []
    
    for i in num1_set:
        if i in num2_set:
            result.append(i)
    return result