class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def is_balanced(num: int) -> bool:
            s = str(num)
            from collections import Counter
            count = Counter(s)
            for digit, freq in count.items():
                if int(digit) != freq:
                    return False
            return True
        
        x = n + 1
        while True:
            if is_balanced(x):
                return x
            x += 1
