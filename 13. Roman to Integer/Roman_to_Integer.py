class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        total = 0 
        n=len(s)
        for i in range(n):
            v = m[s[i]] 
            if i+1 < n and m[s[i]] < m[s[i+1]]:
                total = total - m[s[i]]
            else:
                total = total + m[s[i]]
        return total
                
obj = Solution()
print(obj.romanToInt("III"))       
print(obj.romanToInt("LVIII"))     
print(obj.romanToInt("MCMXCIV"))
