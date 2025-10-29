class Solution:
    def smallestNumber(self, n: int) -> int:
        # Compute k = number of bits needed to represent n
        k = n.bit_length()
        # Compute the smallest number of the form 2^k - 1 that is ≥ n
        answer = (1 << k) - 1
        return answer
