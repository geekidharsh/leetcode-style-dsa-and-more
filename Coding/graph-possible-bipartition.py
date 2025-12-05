"""We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.

 

Example 1:

Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: The first group has [1,4], and the second group has [2,3].
Example 2:

Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Explanation: We need at least 3 groups to divide them. We cannot put them in two groups.
"""

approach:
    # first idea is to get a adjacency list from the given input: gives us all neighbors of a node
    # then form a new group map for each node, mark is None initially
    # iteratively go through each node in adj, if node is not marked then, 
    # dfs: mark node with group label (1 initially), and check for all it's neighbors to be opposite
    # time: o(N+E)
class Solution:
    from collections import defaultdict
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a, b in dislikes:
            adj[a].append(b)
            adj[b].append(a)

        people_group  = {i:None for i in range(1, n+1)}
        
        def dfs(node, grp):
            people_group[node] = grp
            for neigh in adj[node]:
                # check group color of neighbors
                if people_group[neigh] == grp:
                    return False
                if people_group[neigh] == None:
                    if not dfs(neigh, -grp):
                        return False
            return True
        
        for node in adj:
            # print(people_group)
            if people_group[node] is None:
                # this is where we color code 1 or -1
                if not dfs(node, 1):
                    return False
        return True

