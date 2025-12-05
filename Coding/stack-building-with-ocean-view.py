# meta 100
# # There are n buildings in a line. You are given an integer array heights of size n that represents 
# the heights of the buildings in the line.

# The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without 
# obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.


def findBuildings(heights):
    # using monotonic stack to store indices
    stack = []
    n = len(heights)

    for i in range(n):
        # as long as there are items in stack and we get the last index of heights from stack 
        # and compare if current heights is less
        # if less we pop it
        while stack and heights[i] >= heights[stack[-1]]:
            stack.pop()
        # otherwise, current height is less that on the left
        # we keep appending
        stack.append(i)
    
    return stack

heights = [4,2,3,1]
# Output: [0,2,3]

# test 
assert findBuildings(heights) == [0,2,3]