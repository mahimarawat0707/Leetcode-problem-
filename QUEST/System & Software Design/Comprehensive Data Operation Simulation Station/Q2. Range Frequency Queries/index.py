from typing import List
from bisect import bisect_left, bisect_right

class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        # Create a list of lists to store indices for each possible value
        self.l = [[] for _ in range(10001)]
        for i, v in enumerate(arr):
            self.l[v].append(i)

    def query(self, left: int, right: int, v: int) -> int:
        # Count how many times v appears between indices left and right (inclusive)
        return bisect_right(self.l[v], right) - bisect_left(self.l[v], left)


# Example usage
if __name__ == "__main__":
    arr = [1, 2, 1, 3, 1, 2, 2, 3]
    rfq = RangeFreqQuery(arr)
    
    print("Query count of 1 from index 0 to 4:", rfq.query(0, 4, 1))  # Expected: 3
    print("Query count of 2 from index 1 to 6:", rfq.query(1, 6, 2))  # Expected: 3
    print("Query count of 3 from index 3 to 7:", rfq.query(3, 7, 3))  # Expected: 2
