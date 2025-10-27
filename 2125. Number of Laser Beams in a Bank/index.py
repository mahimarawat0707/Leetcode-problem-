from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0   # Number of devices in the previous non-empty row
        total = 0  # Total number of laser beams
        
        # Iterate through each row of the bank
        for row in bank:
            count = row.count('1')  # Count devices in the current row
            
            # Only calculate beams if this row has at least one device
            if count > 0:
                total += prev * count  # Beams between previous and current
                prev = count           # Update previous device count
        
        return total

if __name__ == "__main__":
    bank = ["011001", "000000", "010100", "001000"]
    sol = Solution()
    print("Total Beams:", sol.numberOfBeams(bank))
