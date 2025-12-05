"""Find Median from Data Stream
Hard
Topics: heap, sorting
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, 
and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
"""

# external library usage
# approach, with sorted list - O(m log m)
# where m is the number of inserts
from sortedcontainers import SortedList

class MedianFinder:

    def __init__(self):
        self.num_set = SortedList([])

    def addNum(self, num: int) -> None:
        self.num_set.add(num)
        # print(self.num_set)


    def findMedian(self) -> float:
        n = len(self.num_set)
        if n % 2 == 1:
            median = self.num_set[n//2]
        else:
            median = (self.num_set[n//2] + self.num_set[n//2 - 1]) / 2

        return median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# approach 2 with 2 heaps
# keep two heaps - max and min split in halves for number of inserts
# keep balancing heap when either half is more than 1 bigger in size
# get median
