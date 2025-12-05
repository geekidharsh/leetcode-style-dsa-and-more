# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.
# meta - 2025

def thirdMax(nums):
    # cases: 
        # - nums can have repeated items so make a set()
        # - sort to get the last item as max
        # - if len() is less or equal to 2, then return max else return the thirdmax
         
        s_nums = set(nums)
        if len(s_nums) <= 2:
            return max(s_nums) #o(1)
        else:
            s_nums.remove(max(s_nums)) # o(1)
            s_nums.remove(max(s_nums)) # o(1)
            return max(s_nums) # o(1)

nums = [3,2,1,5,7,9]
thirdMax(nums)

def thirdMaxSpaceOpt(nums):
        max_nums = set()

        for num in nums: # o(n) time, and o(1) space
            if num not in max_nums:
                max_nums.add(num)
            else:
                continue

            if len(max_nums) > 3:
                max_nums.remove(min(max_nums))

        if len(max_nums) < 3:
            return max(max_nums)
        else:
            return min(max_nums)

print(thirdMaxSpaceOpt(nums))