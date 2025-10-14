def rotate(matrix):
    n = len(matrix)
    
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for row in matrix:
        row.reverse()
    return matrix

matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
print("Before rotation:", matrix1)
print("After rotation:", rotate(matrix1))

matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print("\nBefore rotation:", matrix2)
print("After rotation:", rotate(matrix2))