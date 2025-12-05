#meta easy

# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n,
# return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.


def canPlaceFlowers(flowerbed, n):
    # check for every i position, if left and right beds are 0, 
    count = 0

    for i in range(len(flowerbed)):
        # Ensure the current spot is empty
        if flowerbed[i] == 0:
            # check if left and right plots are empty, returns bool
            left_plot = (i == 0) or (flowerbed[i-1] == 0)
            right_plot = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)
            # print(left_plot, right_plot)
        
            if left_plot and right_plot:
                flowerbed[i] = 1
                count += 1
                if count >= n:
                    return True
    return count >= n
