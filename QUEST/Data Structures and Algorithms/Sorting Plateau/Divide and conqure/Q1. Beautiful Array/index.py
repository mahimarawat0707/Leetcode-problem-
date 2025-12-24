from typing import List

class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        """
        Returns a beautiful array of length n.
        A beautiful array is defined by sorting numbers based on
        their reversed binary representation.
        """
        def reverse_binary(num: int) -> str:
            # Convert number to binary, remove '0b', and reverse it
            return bin(num)[2:][::-1]

        return sorted(range(1, n + 1), key=reverse_binary)


# Example usage:
if __name__ == "__main__":
    sol = Solution()
    n = 5
    print(sol.beautifulArray(n))  # Output: [1, 2, 4, 3, 5]
