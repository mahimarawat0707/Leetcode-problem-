from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
            ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
            "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
        ]

        seen = set()

        for word in words:
            transformation = ''.join(morse_code[ord(char) - ord('a')] for char in word)
            seen.add(transformation)

        return len(seen)

if __name__ == "__main__":
    solution = Solution()
    words = ["gin", "zen", "gig", "msg"]
    print("Unique Morse Representations:", solution.uniqueMorseRepresentations(words))
