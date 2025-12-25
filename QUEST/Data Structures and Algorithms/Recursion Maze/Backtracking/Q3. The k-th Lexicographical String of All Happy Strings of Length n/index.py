class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        sz=3*(1<<(n-1))
        if k>sz: return ""

        q, r=divmod(k-1, 1<<(n-1))
        s=[' ']*n
        s[0]=chr(ord('a') + q)
        
        B=format(r, f'0{n-1}b')  # Equivalent to bitset<9> bin(r) with n-1 bits

        xx = [['b', 'c'], ['a', 'c'], ['a', 'b']]
        
        for i in range(n-1):  # Iterating from 0 to n-2
            idx=ord(s[i]) - ord('a')
            s[i+1]=xx[idx][1] if B[i]=='1' else xx[idx][0]

        return "".join(s) 
        