from typing import List

class Solution:
    def maximumHappinessSum(self, christmasJoy: List[int], gifts: int) -> int:
        # Santa gives gifts to the happiest children first
        christmasJoy.sort(reverse=True)

        totalJoy = 0

        for turn in range(gifts):
            currentJoy = christmasJoy[turn] - turn

            if currentJoy <= 0:
                break

            totalJoy += currentJoy

        return totalJoy
