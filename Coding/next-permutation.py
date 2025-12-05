# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
#  then the next permutation of that array is the permutation that follows it in the sorted container.

# For example, for arr = [1,2,3], the following are all the permutations of 
# arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].

# ----------
# solution 1: not for leetcode, understanding only
# does not modify in place
# time: o(n!) * n -> o(n!) factorial of n, since permutation generates all possiblilities
# simple method would be to sort the number and 
# generate all permutations in a list
# get index of the original number in the permutation list
# return idx + 1 as next permutation, if not out of bounds
from itertools import permutations
def get_next_permutation(nums):
    # Convert list to string
    num_str = ''.join(str(i) for i in nums)

    # Get all permutations and sort them lexicographically
    all_permutations = sorted([''.join(p) for p in permutations(num_str)])

    # Find the index of the current permutation
    index = all_permutations.index(num_str)
    
    # Return the next permutation if available
    if index + 1 < len(all_permutations):
        # Convert back to list of integers
        return list(map(int, all_permutations[index + 1]))

# Example usage
nums = [1, 2, 3]
print(get_next_permutation(nums))  # Output: [1, 3, 2]

# -------
# solution: optimal: tricky and impossible to come up on your own
# we observe that for any given sequence that is in descending order, no next larger permutation is possible.
# we go from right, and find the first sequence which satisfy a[i]>a[i−1]
# we need to replace the number a[i−1] with the number which is just larger than itself among the numbers 
# lying to its right section, say a[j].
# swap the numbers a[i−1] and a[j]
# we simply need to reverse the numbers following a[i−1] to get the next smallest lexicographic permutation.

def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    i = len(nums) - 2
    while i >= 0 and nums[i + 1] <= nums[i]:
        i -= 1
    if i >= 0:
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        swap(nums, i, j)
    reverse(nums, i + 1)

def reverse(self, nums, start):
    i, j = start, len(nums) - 1
    while i < j:
        self.swap(nums, i, j)
        i += 1
        j -= 1

def swap(self, nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp
