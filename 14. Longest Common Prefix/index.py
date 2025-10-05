from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for i in range(1, len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""

        return prefix

if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ["flower", "flow", "flight"],
        ["dog", "racecar", "car"],
        ["interspecies", "interstellar", "interstate"],
        ["throne", "dungeon"],
        ["throne", "throne"]
    ]

    for strs in test_cases:
        print(f"Input: {strs} → Longest Common Prefix: '{solution.longestCommonPrefix(strs)}'")
