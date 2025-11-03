from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_cost = 0
        max_time_in_group = neededTime[0]

        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                total_cost += min(max_time_in_group, neededTime[i])
                max_time_in_group = max(max_time_in_group, neededTime[i])
            else:
                max_time_in_group = neededTime[i]

        return total_cost

if __name__ == "__main__":
    colors = "aabaa"
    neededTime = [1, 2, 3, 4, 1]

    sol = Solution()
    result = sol.minCost(colors, neededTime)

    print("Minimum time to remove balloons:", result)
