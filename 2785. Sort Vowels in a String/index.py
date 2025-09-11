class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        
        sorted_vowels = sorted([ch for ch in s if ch in vowels])
        
        i = 0
        result = []
        
        for ch in s:
            if ch in vowels:
                result.append(sorted_vowels[i])
                i += 1
            else:
                result.append(ch)
        
        return "".join(result)
