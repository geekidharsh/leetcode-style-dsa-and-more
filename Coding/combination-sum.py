# topic: recursion, backtrack

# Given an array of distinct integers candidates and a target integer target, 
# return a list of all unique combinations of candidates where the chosen numbers 
# sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. 
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations 
# that sum up to target is less than 150 combinations for the given input.


# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]

# Explanation:
# 2 and 3 are candidates, 
# and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# intuition:
    # need to revise
    # we need to get running list of all combinations - we use a path to keep track
    # use a backtrack approach to recursively call within the iteration of the candidate list
    # keep decreasing target from already found numbers
    # establish base case:
    #   if remaining == 0
        #   add path to result  
        # if remaining < 0 - break
        

candidates = [2,3,6,7]
target = 7

def combination_sum(num, target):
    result = []
    num.sort() #sort for optimization in look up
    
    def backtrack(start, remaining, path):
        for i in range(start, len(num)):
            if remaining == 0:
                # copy path list to result
                result.append(path.copy())
                return
            
            if remaining < 0:
                return
            
            for i in range(start, len(num)):
                # If the candidate is greater than the remaining target, break early.
                if num[i] > remaining:
                    break
                
                path.append(num[i])            
                # Since the same candidate can be chosen multiple times, we pass 'i' instead of 'i+1'
                backtrack(i, remaining - candidates[i], path)
                path.pop()

    backtrack(0, target, [])
    return result

print(combination_sum(candidates, target))
    