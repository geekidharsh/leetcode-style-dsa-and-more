# hard, dp, sorting, arr, binary search

# We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].
# You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no 
# two jobs in the subset with overlapping time range.
# If you choose a job that ends at time X you will be able to start another job that starts at time X.

# Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
# Output: 120
# Explanation: The subset chosen is the first and fourth job. 
# Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    
    # group all values together and sort jobs by end time
    # one all values are sorted by end time asc, it helps to get the next value
    jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
    
    print(jobs)
    n = len(jobs)

    dp = [(0, 0)]  # (end_time, profit)

    for s, e, p in jobs:
        # find insertion point in the dp on the right side, that has an start time >= end_time in the dp
        # float() is for max profit
        i = bisect.bisect_right(dp, (s, float('inf'))) - 1
        print(i, dp)
        current_profit = dp[i][1] + p
        if current_profit > dp[-1][1]:
            dp.append((e, current_profit))

    return dp[-1][1]