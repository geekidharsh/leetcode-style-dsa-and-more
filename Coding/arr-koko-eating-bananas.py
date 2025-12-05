# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
# The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and 
# eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will 
# not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

 

# Example 1:
# Input: piles = [3,6,7,11], h = 8
# Output: 4

# solution:
#     koko has to eat all bananas before time h
#     so we think about starting with speed k = 1. 
#     now, time to eat banana at each pile is = pile/k
#     we iterate this way for all piles of banana. 
#     max speed to each a pile can be at most max(piles)
#     so imagine speed as a sorted arr: [1....k....max]
#     if time exceeds h, then speed has to increase to catch up. so k += 1
#     now, we can imagine a binary search of speed from 1...max
#     if total time less than required we move right, and vice versa - like binary search 
   
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
