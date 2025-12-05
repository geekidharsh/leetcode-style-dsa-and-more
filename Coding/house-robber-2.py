# All houses at this place are arranged in a circle. 
# That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a 
# security system connected, and it will automatically contact the police if two adjacent houses 
# were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, 
# return the maximum amount of money you can rob tonight without alerting the police.

# intuition:
    # similar to house robber but in this the houses are in a circle
    # we split the arr into 2 parts: 1-n, and 0-n-1
    # now we run same algo as houseRobber on both of these and return the max of the two

def houseRobber(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    print(nums[1:])
    print(nums[:-1])

    def helper(nums):
        # let's make an assumption that we have two houses 
        # right before the input array: [house1, house2] + nums
        house1 = 0
        house2 = 0
        for house in nums:
            # house1 + house because we have to skip adjacent house
            curr_max = max(house1 + house, house2) 
            house1 = house2
            house2 = curr_max
        return house2

    return max(helper(nums[1:]), helper(nums[:-1]))