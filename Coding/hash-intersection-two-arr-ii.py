"""Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays 
and you may return the result in any order.


Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
"""

def arrIntersection(nums1, nums2):
    # using sort
    # sorting is the most expensive operation
    # time = o(mlogn + nlogn)
    # space = o(1)
    result = []
    nums1.sort()
    nums2.sort()
    i = j = 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            result.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else: 
            j += 1
            
    return result

print(arrIntersection([1,2,2,1], [2,2]))
print(arrIntersection([4,9,5], [9,4,9,8,4]))

# test
assert arrIntersection([1,2,2,1], [2,2]) == [2, 2]
assert arrIntersection([4,9,5], [9,4,9,8,4]) == [4,9]



def arrIntersectionHash(nums1, nums2):
    # using dictionary

    if len(nums1) < len(nums2):
        return arrIntersectionHash(nums2, nums1)
    else:
        result = {}
        i = j = 0
        while i < len(nums1):
            if nums1[i] == nums2[j]:
                if nums1[i] in result:
                    result[nums1[i]] += 1
                else:
                    result[nums1[i]] = 1
                    j +=1
            i += 1
    return result

print(arrIntersectionHash([1,2,2,1], [2,2]))
print(arrIntersectionHash([4,9,5], [9,4,9,8,4]))
