"""
solvable but need to revise
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and 
then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

Example 1:
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
"""

# approach 1: works but has time limit on leetcode
from typing import List
def findTargetSumWays(nums: List[int], target) -> int:
    # approach is a recursion tree / (like a dfs)
    # at each index we have two options: add or subtract
    # time: 2^n, space: o(n) (recursion stack)
    

    def dfs(curr_idx: int, curr_sum: int):
        # Base case: we've reached the end of the list
        if curr_idx == len(nums):
            if curr_sum == target:
                # If the expression evaluates to target, count it to result
                return 1
            else:
                return 0
        
        # try for both adding and subtracting curr number
        add = dfs(curr_idx + 1, curr_sum + nums[curr_idx])
        sub = dfs(curr_idx + 1, curr_sum - nums[curr_idx])
        return add + sub
        

    result = dfs(0, 0)
    return result

# test 1
nums = [1,1,1,1,1]
target = 3
print(findTargetSumWays(nums, target))

# test 2
nums = [11,20,19,3,25,7,30,45,8,11,35,19,29,9,49,14,22,34,12,0]
target = 34
print(findTargetSumWays(nums, target))


# approach 2: same as 1, with lru_cache
from functools import lru_cache
def findTargetSumWays_lru(nums: List[int], target) -> int:
    
    @lru_cache(maxsize=None)
    def dfs(curr_idx: int, curr_sum: int):
        # Base case: we've reached the end of the list
        if curr_idx == len(nums):
            if curr_sum == target:
                # If the expression evaluates to target, count it to result
                return 1
            else:
                return 0
        
        # try for both adding and subtracting curr number
        add = dfs(curr_idx + 1, curr_sum + nums[curr_idx])
        sub = dfs(curr_idx + 1, curr_sum - nums[curr_idx])
        return add + sub
        

    result = dfs(0, 0)
    return result


# approach 3: dp, without using in-built lru (interview friendly)
from typing import List

def findTargetSumWays(nums: List[int], target: int) -> int:
    """
    DFS with explicit memoization to count the number of expressions 

    Time Complexity: O(n * t)
        - n = len(nums)
        - t = total range of sums (approx. 2 * sum(nums) + 1)
        - Each unique (idx, sum) is computed once.

    Space Complexity: O(n * t) for memo storage + O(n) recursion stack
    """

    memo = {}  # key: (curr_idx, curr_sum), value: # of ways

    def dfs(curr_idx: int, curr_sum: int) -> int:
        # Check if this state has been computed
        if (curr_idx, curr_sum) in memo:
            return memo[(curr_idx, curr_sum)]
        
        # Base case: processed all numbers
        if curr_idx == len(nums):
            return int(curr_sum == target)
        
        # Recursive case: add or subtract current number
        add = dfs(curr_idx + 1, curr_sum + nums[curr_idx])
        sub = dfs(curr_idx + 1, curr_sum - nums[curr_idx])
        
        # Store result in memo
        memo[(curr_idx, curr_sum)] = add + sub
        return memo[(curr_idx, curr_sum)]

    return dfs(0, 0)


