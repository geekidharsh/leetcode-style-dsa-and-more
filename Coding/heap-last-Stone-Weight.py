# topic: heap / priority queue

# You are given an array of integers stones where stones[i] is the weight of the ith stone.

# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. 
# Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.
# Return the weight of the last remaining stone. If there are no stones left, return 0.

# Input: 
stones = [2,7,4,1,8,1]
# Output: 1


def last_stone_weight(stones:int):
    import heapq
    
    # since python has only min heap support we can add -ve to each int to convert to max heap
    stones = [-s for s in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        stone1 = heapq.heappop(stones)
        stone2 = heapq.heappop(stones)
        if stone1 != stone2:
            new = stone1 - stone2
            heapq.heappush(stones, new)
    print(stones)
    return abs(stones[0]) if stones else 0



last_stone_weight(stones)
