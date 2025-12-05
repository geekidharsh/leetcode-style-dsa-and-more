# max consecutive ones - III
# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array 
# if you can flip at most k 0's.
# Example 1:
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6 -> Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Linkedin, Meta, Google, Bloomberg



# approach:
    # left and right window, start left and keep sliding right
    # when a zero is encoundered, update count zero. if current count is > k, break out of it
    # since no more moves allowed
    # at each iteration, keep taking length of sub arr and updating max_len
def maxConsecutiveOnes(nums, k):
    # brute force o(n^2), works but time limit exceed

    max_length = 0
    n = len(nums)
    for left in range(n):
        # Number of 0s in the current window
        # counter resets at each new left 
        count_zeroes = 0
        for right in range(left, n):
            if nums[right] == 0:
                count_zeroes += 1
            
            if count_zeroes > k:
                break
            sub_arr_len = right - left + 1
            max_length = max(max_length, sub_arr_len)
            # print(max_length)
    return max_length


def maxConsecutiveOnesOptimized(nums, k):
    # sliding window, o(n)
    max_length = 0
    n = len(nums)
    left = 0
    count_zero = 0 #Declare count_zero outside the loop
    
    for right in range(n):
        if nums[right] == 0:
            count_zero += 1
        
        while count_zero > k:
            if nums[left] == 0:
                count_zero -= 1
            left += 1
        
        max_length = max(max_length, right - left + 1)
    return max_length