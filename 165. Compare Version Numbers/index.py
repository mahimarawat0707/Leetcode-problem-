class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split both versions by '.'
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        # Get the maximum length between both
        n = max(len(v1), len(v2))
        
        # Compare revision by revision
        for i in range(n):
            # If index out of range, treat as 0
            num1 = int(v1[i]) if i < len(v1) else 0
            num2 = int(v2[i]) if i < len(v2) else 0
            
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
        
        return 0
