class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        zeros = []
        for i, c in enumerate(s):
            if c == '0':
                zeros.append(i)

        Z = len(zeros)
        ans = 0
        
        # Case 1: all-ones substrings
        i = 0
        while i < n:
            if s[i] == '1':
                j = i
                while j < n and s[j] == '1':
                    j += 1
                L = j - i
                ans += L * (L + 1) // 2
                i = j
            else:
                i += 1
        
        # Case 2: substrings with k zeros (1 ≤ k ≤ 199)
        limit = 200
        
        for left in range(Z):
            for k in range(1, limit + 1):
                right = left + k - 1
                if right >= Z:
                    break
                
                # zeros at:
                # zeros[left], zeros[left+1], ..., zeros[right]
                
                L_bound = zeros[left-1] + 1 if left > 0 else 0
                R_bound = zeros[right+1] - 1 if right + 1 < Z else n - 1
                
                # ones inside the zeros span
                inner_ones = (zeros[right] - zeros[left] + 1) - k
                
                need = k * k
                
                if inner_ones >= need:
                    # all left/right choices valid
                    ans += (zeros[left] - L_bound + 1) * (R_bound - zeros[right] + 1)
                    continue
                
                # else we need extra ones from left/right expansions
                deficit = need - inner_ones
                
                # Expand left to count ones
                left_ones = zeros[left] - L_bound
                # Expand right
                right_ones = R_bound - zeros[right]
                
                if left_ones + right_ones < deficit:
                    continue
                
                # Count number of pairs (x,y) such that x + y ≥ deficit
                # x in [0..left_ones], y in [0..right_ones]
                
                # Total possible pairs
                total_pairs = (left_ones + 1) * (right_ones + 1)
                
                # Invalid pairs: x + y < deficit
                # count number of integer pairs inside triangle
                if deficit > left_ones + right_ones:
                    invalid = (left_ones + 1) * (right_ones + 1)
                else:
                    # Triangle area formula
                    invalid = max(0, deficit * (deficit + 1) // 2)
                    if deficit > left_ones:
                        invalid -= ((deficit - left_ones - 1) * (deficit - left_ones) // 2)
                    if deficit > right_ones:
                        invalid -= ((deficit - right_ones - 1) * (deficit - right_ones) // 2)
                
                ans += total_pairs - invalid
        
        return ans
