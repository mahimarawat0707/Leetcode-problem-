class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        # Quick check: if B contains characters not in A, it's impossible
        if not set(B).issubset(set(A)):
            return -1
        
        # Repeat A enough times to cover B
        for i in range(1, len(B) // len(A) + 3):
            if B in A * i:
                return i
        
        return -1  # B not found in repeated A
