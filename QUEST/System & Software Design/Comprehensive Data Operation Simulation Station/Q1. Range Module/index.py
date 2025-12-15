import bisect
from typing import List

class RangeModule:
    def __init__(self):
        # The track list stores interval boundaries in a flattened form:
        # [start1, end1, start2, end2, ...]
        self.track: List[int] = []

    def addRange(self, left: int, right: int) -> None:
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)
        
        subtrack = []
        if start % 2 == 0:
            subtrack.append(left)
        if end % 2 == 0:
            subtrack.append(right)
        
        self.track[start:end] = subtrack

    def removeRange(self, left: int, right: int) -> None:
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)
        
        subtrack = []
        if start % 2 == 1:
            subtrack.append(left)
        if end % 2 == 1:
            subtrack.append(right)
        
        self.track[start:end] = subtrack

    def queryRange(self, left: int, right: int) -> bool:
        start = bisect.bisect_right(self.track, left)
        end = bisect.bisect_left(self.track, right)
        
        return start == end and start % 2 == 1


# Example usage
if __name__ == "__main__":
    rm = RangeModule()
    
    rm.addRange(10, 20)
    print("Query 10-14:", rm.queryRange(10, 14))  # Expected: True
    print("Query 13-15:", rm.queryRange(13, 15))  # Expected: True

    rm.removeRange(14, 16)
    print("Query 13-15 after removal:", rm.queryRange(13, 15))  # Expected: False
    print("Query 16-17:", rm.queryRange(16, 17))  # Expected: True
