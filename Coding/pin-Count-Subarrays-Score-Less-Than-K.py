"""The score of an array is defined as the product of its sum and its length.

For example, the score of [1, 2, 3, 4, 5] is (1 + 2 + 3 + 4 + 5) * 5 = 75.
Given a positive integer array nums and an integer k, return the number of non-empty subarrays of 
nums whose score is strictly less than k.

Input: nums = [2,1,4,3,5], k = 10
Output: 6
Explanation:
The 6 subarrays having scores less than 10 are:
- [2] with score 2 * 1 = 2.
- [1] with score 1 * 1 = 1.
- [4] with score 4 * 1 = 4.
- [3] with score 3 * 1 = 3. 
- [5] with score 5 * 1 = 5.
- [2,1] with score (2 + 1) * 2 = 6.
"""
# hard #prefixsum #twopointer

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # get all prefix sum
        prefix_prod = [0] * (n + 1)
        # we need to get all sub arr prod with score less than k
        # sub arr prod = (sub arr sum) * (len of sub arr)
        # brute force is to iterate and expand for each arr
        # use two pointer approach to calculate curr_sum
        # get score - first time
        # keep shrinking the curr_sum, score using left pointer
        # when condition is met (i.e out of the while loop) - get size of the sub arr and add to result

        left = 0
        curr_sum = 0
        res = 0
        for right in range(n):
            curr_sum += nums[right]
            score = curr_sum * (right - left + 1)
            while score >= k:
                curr_sum -= nums[left]
                left += 1
                score = curr_sum * (right - left + 1)
            res += (right - left + 1)
        return res
            
