# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums 
# being 1 and 2 respectively.

# looks easy but needs revision - for in place solution
def remove_duplicates_from_srt_arr(nums):
    left = 1
    
    for right in range(1, len(nums)):
        if nums[right] != nums[right - 1]:
            nums[left] = nums[right]
            left += 1
    # finally
    for i in range(left, len(nums)):
        nums[i] = '_'

    # print(nums)
    return nums


nums = [0,0,1,1,1,2,2,3,3,4]
print(remove_duplicates_from_srt_arr(nums))