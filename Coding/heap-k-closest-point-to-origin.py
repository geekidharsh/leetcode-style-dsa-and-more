# topic heap, can also be solved with sorting

# Given an array of points where points[i] = [xi, yi]
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
# return the k closest points to the origin (0, 0).


# Input: 
points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq

        # get dist of all points from origin [0,0]
        # add distance along with points to min heap
        # finally pop min heap k times and add it to result
        # k O(logn)

        min_heap = []
        for point in points:
            x, y = point[0], point[1]
            # use dist formula, get sqrt and round to 4
            dist_from_origin = round(sqrt(x**2 + y**2), 4)
            min_heap.append([dist_from_origin, x, y])
        
        heapq.heapify(min_heap)
        result = []
        while k > 0:
            dist, x, y = heapq.heappop(min_heap)
            result.append([x,y])
            k -=1
        return result


            
        