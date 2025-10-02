class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drunk = numBottles
        empty = numBottles
        
        while empty >= numExchange:
            empty -= numExchange
            drunk += 1
            empty += 1
            numExchange += 1
        
        return drunk
