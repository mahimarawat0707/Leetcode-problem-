from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ops = []
        stream_num = 1
        
        for t in target:
            # Push until we reach the target number
            while stream_num < t:
                ops.append("Push")
                ops.append("Pop")
                stream_num += 1
            
            # Push the target number
            ops.append("Push")
            stream_num += 1
        
        return ops

if __name__ == "__main__":
    sol = Solution()

    print(sol.buildArray([1, 3], 3))     # ["Push","Push","Pop","Push"]
    print(sol.buildArray([1, 2, 3], 3))  # ["Push","Push","Push"]
    print(sol.buildArray([1, 2], 4))     # ["Push","Push"]
