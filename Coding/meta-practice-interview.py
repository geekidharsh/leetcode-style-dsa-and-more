# meta practice
"""Question 1
This problem involves handling a large virtual boolean array (N could be up to 1 billion), where only a 
limited number of entries are set to true (via SET queries), and the rest are implicitly false. 
We then need to efficiently find the smallest index ≥ i that is true for each GET query.
Return an array containing the results of all GET queries. The result of queries[i] is the smallest index 
that contains a true value that is greater than or equal to i, or -1 if no index satisfies those conditions.
Example
N = 5
Q = 5
queries = [[2, 3], [1, 2], [2, 1], [2, 3], [2, 2]]
output = [-1, 2, -1, 2]
"""
def answerQueries(queries, N):
  flag_map = {}
  result = [-1] * len(queries)

  for idx, query in enumerate(queries):
    if query[0] == 1:
        flag_map[query[1]] = True

    if query[1] in flag_map and flag_map[query[1]]:
      result[idx] = query[1]
    else:
      result[idx] = -1
  
  return result

# correct solution
from sortedcontainers import SortedList
def answerQueries(queries, N):
    true_indices = SortedList()
    result = []

    for qtype, index in queries:
        if qtype == 1:
            true_indices.add(index)
        elif qtype == 2:
            pos = true_indices.bisect_left(index)
            if pos < len(true_indices):
                result.append(true_indices[pos])
            else:
                result.append(-1)
    return result

"""Question 2
You are given an array A containing N integers. Your task is to find all subarrays whose average sum is greater 
than the average sum of the remaining array elements. You must return the start and end index of each subarray in 
sorted order.
A subarray that starts at position L1 and ends at position R1 comes before a subarray that starts at L2 and ends 
at R2 if L1 < L2, or if L1 = L2 and R1 ≤ R2.
Note that we'll define the average sum of an empty array to be 0, and we'll define the indicies of the array 
(for the purpose of output) to be 1 through N. A subarray that contains a single element will have L1 = R1.
Signature
Subarray[] aboveAverageSubarrays(int[] A)
Input
1 ≤ N ≤ 2,000
1 ≤ A[i] ≤ 1,000,000
Output
A Subarray is an object with two integer fields, left and right, defining the range that a given subarray covers. 
Return a list of all above-average subarrays sorted as explained above.
Example 1
A = [3, 4, 2]
output = [[1, 2], [1, 3], [2, 2]]
The above-average subarrays are [3, 4], [3, 4, 2], and [4].
"""

def aboveAvgSubarr(A):
    N = len(A)
    prefix_sum = [0] * (N+1) # [0,3,7,9]
    
    # get prefix sum for each i position
    for i in range(N):
        prefix_sum[i+1] = prefix_sum[i] + A[i]

    # last element will have sum(A)
    total_sum = prefix_sum[N] # 9
    result = []
    
    # get all sub arr sum
    for i in range(N): 
        for j in range(i, N): 
            subarr_sum = prefix_sum[j + 1] - prefix_sum[i] # 3
            sub_len = j - i + 1 # 1
            rem_len = N - sub_len # 3-1 = 2
            rem_sum = total_sum - subarr_sum # 6
            
            if rem_len == 0:
                if subarr_sum > 0:
                    result.append([i+1, j+1])
            else:
                # now to get above avg: 
                # subarr_sum / sub_len > rem_sum / rem_len... instead we use cross multiplication
                if subarr_sum * rem_len > rem_sum * sub_len: # 6 > 3
                    result.append((i + 1, j + 1))
    result.sort()
    return result