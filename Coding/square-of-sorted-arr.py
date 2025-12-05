# Given an integer array nums sorted in non-decreasing order, return an array of the squares 
# of each number sorted in non-decreasing order.

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].


import heapq


def square_sorted_arr(nums):
    result_heap = []
    for item in nums:
        res = item * item
        heapq.heappush(result_heap, res)
    
    temp = []
    while len(result_heap):
        temp.append(heapq.heappop(result_heap))
    print(temp)
    


nums = [-4,-1,0,3,10]

square_sorted_arr(nums)