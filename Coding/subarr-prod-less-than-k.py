# Given an array of integers nums and an integer k, return the number of 
# contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

 

# Example 1:

# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.


nums = [10,5,2,6] 
k = 100

# solution
# optimal solution is linear, involves sliding window
# add new counts at the end of each iterations

def subarr_prod_lessthan_k(nums, k):
    if k < 1:
        return 0

    result = 0
    left = 0
    prod = 1
    for right in range(len(nums)):
        prod = prod * nums[right] # get current product
        while left <= right and prod >= k:
            prod = prod // nums[left]
            left += 1
        result += right - left + 1 # +1 is used because the element itself is a subarr
    return result
print(subarr_prod_lessthan_k(nums, k))