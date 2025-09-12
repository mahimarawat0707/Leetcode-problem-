from typing import List

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag_sq = 0
        max_area = 0

        for width, height in dimensions:
            diag_sq = width * width + height * height
            area = width * height

            if diag_sq > max_diag_sq:
                max_diag_sq = diag_sq
                max_area = area
            elif diag_sq == max_diag_sq:
                max_area = max(max_area, area)
        return max_area
    
if __name__ == "__main__":
    solution = Solution()
    dimensions =  [[9,3],[8,6]]
    print("Max Area with Max Diagonal:", solution.areaOfMaxDiagonal(dimensions))