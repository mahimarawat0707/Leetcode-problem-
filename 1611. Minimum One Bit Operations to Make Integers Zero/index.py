class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        # Reverse Gray Code decoding
        result = n
        result ^= result >> 1
        result ^= result >> 2
        result ^= result >> 4
        result ^= result >> 8
        result ^= result >> 16
        return result
