"""
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] 
indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true

Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
"""
# pinterest, meta
# bfs, disjointed set, graph, cycle detection in graph

def validTree(self, n: int, edges: List[List[int]]) -> bool:
    # if given graph is tree:
    # all nodes are connected
    # there are no cycles
    # no trick, this question is purely dsa for union-find - revise union-find
    
    # graph of n nodes must have n-1 edges for a tree
    if len(edges) != n - 1:
        return False
    
    # compress
    # each node is it's own parent initially
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]  # Path compression
            x = parent[x]
        return x
    
    #  Union function to connect two nodes
    def union(x,y):
        root_x = find(x)
        root_y = find(y)
        if root_x == root_y:
            # If roots are the same, a cycle exists
            return False
        # Union the two sets by connecting one root to the other
        parent[root_y] = root_x
        return True
    
    for x, y in edges:
        # iterate over all edges
        if not union(x, y):
            return False
    # if all unions succeed, return true
    return True
