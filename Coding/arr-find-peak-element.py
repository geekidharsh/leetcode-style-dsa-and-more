#meta

# we keep comparing i with i+1, on each move 
# if it's true, return the index, else at the end last elem is the peak - it was a rising slope
# trick: 
    # binary search style approach works, even though given arr is not 'really' sorted. this is because of the 
    # condition of peak as defined in question: i-1 < i > i + 1

nums = [1,2,3,1]

def findPeak(nums):
    # o(n)
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            return i
            
    # we reached the end and it was a rising list of nums
    return len(nums) - 1


def findPeakOpt(nums):
    # binary search approach to o(logn)
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left