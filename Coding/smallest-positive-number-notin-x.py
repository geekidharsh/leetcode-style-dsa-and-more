
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.


A = [1, 3, 6, 4, 1, 2]

def solution(A):
    A.sort()
    first = min(A)
    last = max(A)
    total_range = [i for i in range(first+1, last)]
    for i in total_range:
        if i in   
    

    return num


print(solution(A))