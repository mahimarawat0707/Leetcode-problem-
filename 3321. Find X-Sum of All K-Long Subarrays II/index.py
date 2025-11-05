# solution.py
# File path: solution.py

from collections import defaultdict

# Try to import SortedList; if not available provide a simple fallback.
try:
    from sortedcontainers import SortedList  # type: ignore
except Exception:
    # Minimal pure-Python SortedList replacement sufficient for this code's usage.
    import bisect
    from typing import Iterable, List, Any, Optional

    class SortedList:
        """Simple fallback SortedList using bisect; supports methods used in solution."""
        def __init__(self, iterable: Optional[Iterable[Any]] = None):
            self._data: List[Any] = sorted(iterable) if iterable is not None else []

        def add(self, item: Any) -> None:
            bisect.insort(self._data, item)

        def remove(self, item: Any) -> None:
            # find leftmost occurrence and remove; raise ValueError if not found
            i = bisect.bisect_left(self._data, item)
            if i == len(self._data) or self._data[i] != item:
                raise ValueError(f"{item} not in SortedList")
            self._data.pop(i)

        def pop(self, index: int = -1) -> Any:
            return self._data.pop(index)

        def __len__(self) -> int:
            return len(self._data)

        def __getitem__(self, index):
            return self._data[index]

        def __contains__(self, item: Any) -> bool:
            i = bisect.bisect_left(self._data, item)
            return i != len(self._data) and self._data[i] == item

        def __bool__(self):
            return bool(self._data)

        def __repr__(self) -> str:
            return f"SortedList({self._data!r})"


class Solution:
    def findXSum(self, nums, k, x):
        freq = defaultdict(int)

        # Sorted by (frequency ascending, value ascending)
        best = SortedList()
        others = SortedList()
        ans = []
        score = 0

        def add(val):
            nonlocal score
            old = freq[val]
            freq[val] += 1
            now = freq[val]

            tup_old = (old, val)
            tup_new = (now, val)

            if old > 0:
                if tup_old in best:
                    best.remove(tup_old)
                    score -= old * val
                else:
                    others.remove(tup_old)

            others.add(tup_new)
            rebalance()

        def remove(val):
            nonlocal score
            old = freq[val]
            freq[val] -= 1
            now = freq[val]

            tup_old = (old, val)
            tup_new = (now, val)

            if tup_old in best:
                best.remove(tup_old)
                score -= old * val
            else:
                others.remove(tup_old)

            if now > 0:
                others.add(tup_new)

            rebalance()

        def rebalance():
            nonlocal score
            # Fill best until size == x
            while len(best) < x and len(others) > 0:
                cand = others.pop()  # largest by tuple (freq, val)
                best.add(cand)
                score += cand[0] * cand[1]

            # Swap if others has a better candidate (compare tuples)
            while len(others) > 0 and len(best) > 0 and others[-1] > best[0]:
                low = best.pop(0)
                high = others.pop()

                score -= low[0] * low[1]
                score += high[0] * high[1]

                best.add(high)
                others.add(low)

        # guard: if k > len(nums) treat as single window
        if k <= 0:
            return []

        # initialize first window
        for i in range(min(k, len(nums))):
            add(nums[i])

        if len(nums) >= k:
            ans.append(score)
        else:
            # if window smaller than k, still return score for that window
            ans.append(score)

        # slide window
        for i in range(k, len(nums)):
            remove(nums[i - k])
            add(nums[i])
            ans.append(score)

        return ans


if __name__ == "__main__":
    # Quick smoke tests
    s = Solution()

    # Example 1
    nums = [1, 2, 1, 3, 2]
    k = 3
    x = 2
    print("nums:", nums, "k:", k, "x:", x)
    print("result:", s.findXSum(nums, k, x))

    # Example 2 (edge cases)
    nums = [5, 5, 5]
    k = 2
    x = 1
    print("nums:", nums, "k:", k, "x:", x)
    print("result:", s.findXSum(nums, k, x))

    # If you see ModuleNotFoundError earlier, install the package:
    print("\nIf you prefer the real SortedList, run: pip install sortedcontainers")
