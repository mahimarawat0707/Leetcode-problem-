from functools import lru_cache

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)

        @lru_cache(None)
        def dp(i: int, can_change: bool, mask: int) -> int:
            """
            Return the maximum number of *cuts* (i.e. partitions minus one) from s[i:]
            with the given state (whether we can still change one character, and current mask of distinct letters in this ongoing partition).
            """
            if i == n:
                # no more characters → no further cuts
                return 0

            # Helper: try using a newBit (either from original char or changed) and decide whether it causes a new partition
            def try_with(new_bit: int, next_can_change: bool) -> int:
                new_mask = mask | new_bit
                # if adding this character makes distinct count exceed k → we must start a new partition
                if new_mask.bit_count() > k:
                    # we “cut” before this character, so +1 partition, and new partition starts with this newBit
                    return 1 + dp(i + 1, next_can_change, new_bit)
                else:
                    # still within same partition
                    return dp(i + 1, next_can_change, new_mask)

            res = 0
            # Option 1: use s[i] as is
            orig_bit = 1 << (ord(s[i]) - ord('a'))
            res = max(res, try_with(orig_bit, can_change))

            # Option 2: if we still can change, try changing s[i] to any other letter
            if can_change:
                # Try all 26 possible letters
                for j in range(26):
                    bit_j = 1 << j
                    # If bit_j is same as orig_bit, that’s equivalent to no change, so skip
                    if bit_j == orig_bit:
                        continue
                    res = max(res, try_with(bit_j, False))

            return res

        # dp returns the number of *extra cuts* (i.e. partitions beyond the first). So total partitions = dp(...) + 1
        return dp(0, True, 0) + 1
