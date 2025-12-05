# There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.
# You are given two integer array position and speed, both of length n, where position[i] is the starting 
# mile of the ith car and speed[i] is the speed of the ith car in miles per hour.

# A car cannot pass another car, but it can catch up and then travel next to it at the speed of 
# the slower car. A car fleet is a car or cars driving next to each other. The speed of the car 
# fleet is the minimum speed of any car in the fleet.

# Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
# Output: 3


target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

def carFleet(target, position, speed):
    # as long as car pos and speed is there, it doesnt matter how arr is organized so sort them together
    # create pairs of pos and speed and sort in reverse order to get sorted pairs
    pos_speed = sorted(zip(position, speed), reverse=True)
    print(pos_speed)

    stack = []
    for item in pos_speed:
        # time it takes for curr car to reach target
        c_pos = item[0]
        c_speed = item[1]
        c_time = (target - c_pos) / c_speed
        stack.append(c_time)
        
        # if a new car exceeds target, fleet can't be formed so pop
        if len(stack) > 1 and stack[-1] <= stack[-2]:
            stack.pop()
    
    return len(stack)


print(carFleet(target, position, speed))