from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0:
                empty_left = (i == 0 or flowerbed[i - 1] == 0)
                empty_right = (i == length - 1 or flowerbed[i + 1] == 0)

                if empty_left and empty_right:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True

        return count >= n


if __name__ == "__main__":
    solution = Solution()

    flowerbed1 = [1, 0, 0, 0, 1]
    n1 = 1
    print("Can place?", solution.canPlaceFlowers(flowerbed1, n1))  # ✅ Expected: True

    flowerbed2 = [1, 0, 0, 0, 1]
    n2 = 2
    print("Can place?", solution.canPlaceFlowers(flowerbed2, n2))  # ❌ Expected: False
