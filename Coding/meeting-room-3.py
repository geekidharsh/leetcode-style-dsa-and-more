"""
You are given an integer n. There are n rooms numbered from 0 to n - 1. i.e: n=2 (two rooms: 0 and 1)
You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held 
during the half-closed time interval [starti, endi). All the values of starti are unique.

Meetings are allocated to rooms in the following manner:

Each meeting will take place in the unused room with the lowest number.
    If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting 
    should have the same duration as the original meeting.
    When a room becomes unused, meetings that have an earlier original start time should be given the room.
    Return the number of the room that held the most meetings. If there are multiple rooms, return the room 
    with the lowest number.
Input: n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
Output: 0

Explanation:
- At time 0, both rooms are not being used. The first meeting starts in room 0.
- At time 1, only room 1 is not being used. The second meeting starts in room 1.
- At time 2, both rooms are being used. The third meeting is delayed.
- At time 3, both rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 1 finishes. The third meeting starts in room 1 for the time period [5,10).
- At time 10, the meetings in both rooms finish. The fourth meeting starts in room 0 for the time period [10,11).
Both rooms 0 and 1 held 2 meetings, so we return 0 (room with lowest number) 

"""


# Input: 
n = 2
meetings = [[0,10],[1,5],[2,7],[3,4]]

from typing import *
import heapq
def mostBooked(n: int, meetings: List[List[int]]) -> int:
    # Sort the meetings by start time
    meetings.sort()
    available_rooms = list(range(n))  # all rooms initially available
    occupied_rooms = []       # no rooms occupied at the start
    meeting_counts = [0] * n   # each room has 0 meetings initially

    for start, end in meetings:
        # Free up rooms that are done before current meeting starts
        while occupied_rooms and occupied_rooms[0][0] <= start:
            _, room = heapq.heappop(occupied_rooms)
            heapq.heappush(available_rooms, room)

        duration = end - start
        if available_rooms:
            # Assign to the lowest-numbered available room
            room = heapq.heappop(available_rooms)
            heapq.heappush(occupied_rooms, (end, room))
        else:
            # No room available; delay until a room is free
            earliest_end, room = heapq.heappop(occupied_rooms)
            new_end = earliest_end + duration
            heapq.heappush(occupied_rooms, (new_end, room))
        meeting_counts[room] += 1

    # Return the room with most meetings; if tie, lowest number
    max_meetings = max(meeting_counts)
    for i in range(n):
        if meeting_counts[i] == max_meetings:
            return i

mostBooked(n, meetings)