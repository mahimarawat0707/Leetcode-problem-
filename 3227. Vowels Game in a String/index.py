class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = set("aeiou")
        for ch in s:
            if ch in vowels:
                return True
        return False
