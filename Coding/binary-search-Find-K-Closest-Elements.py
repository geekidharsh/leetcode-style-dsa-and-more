"""
tricky question

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array.
The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:
|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
"""


# approach:
# one of the trickiest binary search problems
# find k numbers that are closest to x
# two pointer, get mid based on k count
# result should also be sorted in ascending order.
# check which window of x - window point is better to look
# potential starting point is arr[mid]
# x - arr[mid] - left window closest to x 
# arr[mid + k] - x  - right window closest to x
# if right window is closest, we move left = mid + 1
def findClosestElements(arr, k, x):

    # Base case
    if len(arr) == k:
        return arr
    
    left = 0
    right = len(arr) - k 
    # k, not n right most side we are interested in should begin at k and not n, 
    # so as to find k elements to the right of it.
    
    
    while left < right:
        mid = (left + right) // 2
        print(arr[mid], arr[left], arr[right])
        # check which window of x - window point is better to look
        # potential starting point is arr[mid]
        # x - arr[mid] - left window closest to x 
        # arr[mid + k] - x  - right window closest to x
        # if right window is closest, we move left = mid + 1
        if (x - arr[mid]) > (arr[mid + k] - x):
            left = mid + 1
        else:
            right = mid
        
    return arr[left:left+k]