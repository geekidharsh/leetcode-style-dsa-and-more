from collections import Counter

def getLargestOutlier(nums):
        # get total sum and a num_set counter
        # outlier is:
        # outlier = total_sum - 2*(special_sum)
        # we iterate through items, check if current item is outlier or not
        tot_sum = sum(nums)
        num_set = Counter(nums) 
        outliers = float('-inf') # start with smallest value possible: -inf

        for item in nums:
            pot_outlier = tot_sum - 2*item
            if pot_outlier in num_set:
                if pot_outlier != item or num_set[item] > 1:
                    outliers = max(outliers, pot_outlier)
        print(outliers)
        return outliers


# Input: 
nums = [2,3,5,10]
# The special numbers could be 2 and 3, thus making their sum 5 and the outlier 10.
# Output: 10

getLargestOutlier(nums)