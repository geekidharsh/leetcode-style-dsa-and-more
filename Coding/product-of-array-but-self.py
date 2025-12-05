# Given an integer array nums, return an array answer such that 
# answer[i] is equal to the product of all the elements of nums except nums[i].

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]


nums = [1,2,3,4]

def prodOfEverythingExcept(nums):
    answer = []
    product = 1
    zeroes = []
    for i in range(len(nums)):
        if nums[i] == 0:
            zeroes.append(i)
        else:
            product *= nums[i]
    if len(zeroes) > 1:
        answer = [0]*len(nums)
        return answer

    if len(zeroes) == 1 :
        answer = [0]*len(nums)
        answer[zeroes[0]] = product
        return answer
    for i in range(len(nums)):
        answer.append(product//nums[i])
    return answer



def prodOfEverythingExceptOptimized(nums):
    answer = []
    product = 1
    zerosCount = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            zerosCount ++
            ZeroIndex = i
        else:
            product *= nums[i]
    if zerosCount > 1:
        answer = [0]*len(nums)
        return answer
    elif zerosCount == 1 :
        answer = [0]*len(nums)
        answer[ZeroIndex] = product
        return answer
    for i in range(len(nums)):
        answer.append(product//nums[i])
    return answer
    
print(prodOfEverythingExceptOptimized(nums))