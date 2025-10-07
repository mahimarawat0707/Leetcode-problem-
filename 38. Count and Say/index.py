class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        result = "1"
        
        for _ in range(n - 1):
            temp = ""
            count = 1
            
            for i in range(1, len(result)):
                if result[i] == result[i - 1]:
                    count += 1
                else:
                    temp += str(count) + result[i - 1]
                    count = 1
            temp += str(count) + result[-1]
            
            result = temp
        
        return result
