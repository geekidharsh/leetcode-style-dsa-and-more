# Reshape the Matrix
"""
Reshape a m x n matrix into a new one with a different size r x c keeping 
its original data.

You are given an m x n matrix mat and two integers r and c representing the
number of rows and the number of columns of the wanted reshaped matrix.

Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]
"""

# time: o(m*n)

def reshapeMatrix(mat, R, C):
    n = len(mat)
    m = len(mat[0])

    if n*m != R*C: return mat
    else:
        queue = []
        result = [[None for _ in range(C)] for _ in range(R)]
        for row in range(n):
            for col in range(m):
                queue.append(mat[row][col])
        i = 0
        for k in range(R):
            for m in range(C):
                result[k][m] = queue[i]
                i += 1
        return result



mat = [[1,2],[3,4]]
r = 1
c = 4

m1 = [[1,2],[3,4]]
r1 = 2
c1 = 4


m2 = [[1,2],[3,4]]
r2 = 4
c2 = 1
print(reshapeMatrix(mat, r, c))
print(reshapeMatrix(m1, r1, c1))
print(reshapeMatrix(m2, r2, c2))