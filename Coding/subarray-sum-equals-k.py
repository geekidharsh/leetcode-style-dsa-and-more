# Given an array of integers nums and an integer k, 
# return the total number of continuous subarrays whose sum equals to k.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2

nums = [1,1,1]
k = 2

def subarraySumEqualsK(nums, k):
    prefixSums = {0:1}
    currentSum = 0
    result = 0
    for i in range(len(nums)):
        currentSum += nums[i]
        diff = k - currentSum
        if currentSum not in prefixSums:
            prefixSums[currentSum] = 1 
        else:
            prefixSums[currentSum] += 1
    print(prefixSums)

subarraySumEqualsK(nums, k)
