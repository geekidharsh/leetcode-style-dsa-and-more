# Given an integer array nums and an integer k, return the k most frequent elements. 
# You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# intuition: hashmap, max heap, sorting

from collections import Counter
def topKFrequent(nums, k):
    # create a freq_count list of of size len(nums), each index will store 
    # now sort keys by their values (in reverse for -ve) to get max-to-min frequency
    # of keys, also can use reverse=True
    # counter.items() returns a list of key-value pairs
    # key=lambda x: x[1]) sorts the list of tuples based on the second element (value).

    count = Counter(nums)
    frequency_map = sorted(count.items(), key=lambda x: -x[1])
    result = []

    for idx in range(k):
        result.append(frequency_map[idx][0])
    return result


nums = [1,1,1,2,2,3]
k = 2

topKFrequent(nums, k)