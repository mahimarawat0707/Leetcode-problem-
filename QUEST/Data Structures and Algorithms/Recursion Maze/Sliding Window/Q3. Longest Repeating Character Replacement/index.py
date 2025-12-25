class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        store = [0] * 26
        l = 0
        max_freq = 0
        result = 0

        for r in range(len(s)):
            idx = ord(s[r]) - ord('A')
            store[idx] += 1
            max_freq = max(max_freq, store[idx])

            window_size = r - l + 1

            if window_size - max_freq > k:
                store[ord(s[l]) - ord('A')] -= 1
                l += 1

            result = max(result, r - l + 1)

        return result
