"""You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 
1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. 
You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.
Example 1:

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6."""

# approach: 
# came up on my own base approach
# create a map of stops and all buses that go to it
# use a queue, since we need to check buses along route from left to right
# use bfs approach keep track of visited buses and visited stops

# time and space both are: 
    # O(S) for building the map +O(S) for checking every stop +O(S) every stop in the route = O(S)
    # where S is number of stops
    # in simple terms, length of routes + length of stops (nodes and edges in bfs )
# from typing import *
# from collections import deque


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        """check routes between two stops, 
        returns number of buses taken between them"""  
        # if source and target is the same stop, no bus taken
        if source == target:
            return 0

        # hashmap to create grouping of stops and buses that go to them
        stop_map = {}
        for bus, stops in enumerate(routes):
            for stop in stops:
                if stop not in stop_map:
                    stop_map[stop] = [bus]
                else:
                    stop_map[stop].append(bus)

        # If either source or target is unreachable from any bus
        if source not in stop_map or target not in stop_map:
            return -1

        # print(stop_map)
        
        queue = deque() # (bus, number_of_bus_taken)
        visited_stops = set()
        visited_buses = set()

        for bus in stop_map[source]:
            if bus not in visited_buses:
                visited_buses.add(bus)
                queue.append([bus, 1])
        
        while queue:
            curr_bus, buses_taken = queue.popleft()

            # check all stops in the route of current bus
            for stop in routes[curr_bus]:
                # if stop is target, we've found it. return buses_taken count
                if stop == target:
                    return buses_taken
            
                if stop not in visited_stops:
                    visited_stops.add(stop)
                    for next_bus in stop_map[stop]:
                        if next_bus not in visited_buses:
                            visited_buses.add(next_bus)
                            queue.append([next_bus, buses_taken+1])
        return -1

