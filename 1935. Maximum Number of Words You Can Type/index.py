class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        count = 0

        for word in text.split():
            if all(ch not in broken for ch in word):
                count += 1

        return count
