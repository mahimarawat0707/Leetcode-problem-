def findMostFrequentVowelAndConsonant(s: str) -> int:
    vowels = set("aeiou")
    freq = {}
    
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    
    max_vowel = 0
    max_consonant = 0
    
    for ch, f in freq.items():
        if ch in vowels:
            max_vowel = max(max_vowel, f)
        else:
            max_consonant = max(max_consonant, f)
    
    return max_vowel + max_consonant


# Example test cases
if __name__ == "__main__":
    s1 = "successes"
    s2 = "aeiaeia"
    
    print("Input:", s1, "-> Output:", findMostFrequentVowelAndConsonant(s1))  # Expected 6
    print("Input:", s2, "-> Output:", findMostFrequentVowelAndConsonant(s2))  # Expected 3
