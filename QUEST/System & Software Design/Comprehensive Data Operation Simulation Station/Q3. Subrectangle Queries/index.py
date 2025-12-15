from typing import List

class SubrectangleQueries:
    def __init__(self, rectangle: List[List[int]]):
        self.r = rectangle        

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                self.r[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.r[row][col]


# Example usage
if __name__ == "__main__":
    rectangle = [
        [1, 2, 1],
        [4, 3, 4],
        [3, 2, 1],
        [1, 1, 1]
    ]

    obj = SubrectangleQueries(rectangle)
    print("Initial value at (0, 2):", obj.getValue(0, 2))  # Expected: 1
    
    obj.updateSubrectangle(0, 0, 3, 2, 5)
    print("Value at (0, 2) after update:", obj.getValue(0, 2))  # Expected: 5
    print("Value at (3, 1) after update:", obj.getValue(3, 1))  # Expected: 5
