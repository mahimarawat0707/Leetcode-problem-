class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        empty = numBottles
        
        while empty >= numExchange:
            new_bottles = empty // numExchange
            total += new_bottles
            empty = empty % numExchange + new_bottles
        
        return total
