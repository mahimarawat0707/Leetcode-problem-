from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        total = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1 and i > 0 and j > 0:
                    matrix[i][j] = 1 + min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])
                total += matrix[i][j]

        return total


if __name__ == "__main__":
    solution = Solution()

    matrix1 = [
        [0,1,1,1],
        [1,1,1,1],
        [0,1,1,1]
    ]
    print("Total squares:", solution.countSquares(matrix1)) 

    matrix2 = [
        [1,0,1],
        [1,1,0],
        [1,1,0]
    ]
    print("Total squares:", solution.countSquares(matrix2))
