"""277 - Find the Celebrity
Suppose you are at a party with n people labeled from 0 to n - 1 and among them, there may exist one celebrity

condition
- everyone knows celebrity
- celebrity does not know anyone.
- return label of the celebrity or -1 of there are no celebrities.

given: 
    - An api: knows(a, b) -> bool 
"""


graph = [[1,1,0],[0,1,0],[1,1,1]]

def findCelebrity(n):
    # greedy approach:
    candidate = 0
    for i in range(1, n):
        if knows(candidate, i):
            candidate = i
    
    for i in range(n):
        if candidate == i:
            continue
        
        if knows(candidate, i) or not knows(i, candidate):
            return -1
    
    return candidate