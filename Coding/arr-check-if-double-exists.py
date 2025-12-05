# given an arr of integers (+ve or -ve), check if for any i != j, 
# there exists a arr[i] = 2 * arr[j]
# arr : [10,2,5,3], return True

def checkIfExists(arr):
    arr.sort()

    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] == 2 * arr[right] or arr[right] == 2 * arr[left]:
            return True
        elif 2 * arr[left] < arr[right]:
            left += 1
        else:
            right -=1
    return False


arr = [-20,8,-6,-14,0,-19,14,4]
assert checkIfExists(arr) == True