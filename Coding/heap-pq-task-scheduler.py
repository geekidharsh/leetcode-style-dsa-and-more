# You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be 
# idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: 
# there has to be a gap of at least n intervals between two tasks with the same label.

# Return the minimum number of CPU intervals required to complete all tasks.
# Example 1:
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8

# Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

# After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, 
# neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

tasks = ["A","A","A","B","B","B"]
n = 2

def task_scheduler(tasks, n):
    # we need to make a priority queue - max heap to get task in the order of priority,
    # we prioritize based on occurance count so a hash count is good here
    # since every task will take 1 unit to complete
    # we make a queue for executing tasks based on maxheap - queue will have
    # task count, time when it will be ready next: curr place in time + n

    from collections import Counter, deque
    import heapq
    t_counter = Counter(tasks)
    
    max_heap = [-v for v in t_counter.values()]
    heapq.heapify(max_heap)
    # print(max_heap)
    
    time_ct = 0
    q = deque() # [-v, idletime]
    
    while max_heap or q:
        time_ct += 1
        
        if max_heap: # if there are task in heap, take and add them to queue for processing
            # decrease task count
            val = 1 + heapq.heappop(max_heap) # we add instead of sub since we store in -ve for max heap in python
            if val: 
                q.append([val, time_ct + n])
        
        if q and q[0][1] == time_ct: # if tasks are in queue and task's time matches with curr time
            val = q.popleft()[0]
            heapq.heappush(max_heap, val)
    return time_ct     

# test code
assert task_scheduler(tasks, n) == 8
assert task_scheduler(tasks=["A","C","A","B","D","B"], n=1) == 6    