# meta 100
# You are given a sorted array that has been rotated at an unknown pivot point, 
# along with a target value. Develop an algorithm to locate the index of the target value in the array. 
# If the target is not present, return -1. The algorithm should have a time complexity of O(log n).

# Input: 
nums = [4,5,6,7,0,1,2]
target = 0
# Output: 4


def search(nums, target):
        # goal is to find the pivot index
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            # check if left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1