"""This problem is an extension of Nested List Weight Sum, where we need to find the sum of each integer multiplied by its depth. 
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. 
The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth. 

Let maxDepth be the maximum depth of any integer.

The weight of an integer is maxDepth - (the depth of the integer) + 1. Return the sum of each integer in nestedList
multiplied by its weight.

Input: nestedList = [[1,1],2,[1,1]]
Output: 8
Explanation: Four 1's with a weight of 1, one 2 with a weight of 2.
1*1 + 1*1 + 2*2 + 1*1 + 1*1 = 8

"""

# nested weight sum - 1 is the prior question to solve, in this extension need to compute weight
# max depth is needed, to get that using dfs compute hashmap to find all values at each depth
# finally get total sum is easy once hashmap is ready
def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
    # weight = max_depth - (depth of integer) + 1
    depth_map = {}
    def dfs(nestedList, depth):
        for item in nestedList:
            if item.isInteger():
                if depth in depth_map:
                    depth_map[depth].append(item.getInteger())
                else:
                    depth_map[depth] = [item.getInteger()]
            else:
                dfs(item.getList(), depth + 1)
    dfs(nestedList, 1)

    # get max depth from all depths
    max_depth = max(depth_map.keys())
    total = 0
    for depth, vals in depth_map.items():
        weight = max_depth - depth + 1
        level_sum = sum(vals) * weight
        total += level_sum

    print(depth_map, max_depth)
    return total