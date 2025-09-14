from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        exact_words = set(wordlist)
        
        case_insensitive = {}
        
        vowel_error = {}
        
        vowels = set('aeiou')
        
        def mask(word):
            return ''.join('*' if ch in vowels else ch for ch in word)
        
        for word in wordlist:
            lower_word = word.lower()
            
            if lower_word not in case_insensitive:
                case_insensitive[lower_word] = word
            
            masked = mask(lower_word)
            if masked not in vowel_error:
                vowel_error[masked] = word
        
        result = []
        for query in queries:
            if query in exact_words:
                result.append(query)
            else:
                lower_query = query.lower()
                if lower_query in case_insensitive:
                    result.append(case_insensitive[lower_query])
                else:
                    masked = mask(lower_query)
                    if masked in vowel_error:
                        result.append(vowel_error[masked])
                    else:
                        result.append("")
        return result
