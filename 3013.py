class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        heap_used, heap_unused, used = [], [], set()
        s, ans = 0, inf
        for right in range(1, len(nums)):
            left = right - dist - 1

            # Move the left border of the window
            if left > 0 and left in used:
                    # If the left element was used in calculating the cost, then we delete it
                used.remove(left)
                s -= nums[left]

                    # Find the smallest unused element within the window boundary
                while heap_unused and heap_unused[0][1] < left:
                    heappop(heap_unused)

                if heap_unused: # If it exists, use it to calculate the cost
                    num, i = heappop(heap_unused)
                    heappush(heap_used, (-num, i))
                    used.add(i)
                    s += num

            # Move the right border of the window
            if len(used) < k - 1:
                # If less than k-1 elements are used, use the added element to calculate the cost
                heappush(heap_used, (-nums[right], right))
                used.add(right)
                s += nums[right]
            else:
                    #Find the largest used element
                while heap_used[0][1] not in used:
                    heappop(heap_used)
                
                if nums[right] < -heap_used[0][0]:
                        # If it is larger than the element being added to the window, replace it
                    num, i = heapreplace(heap_used, (-nums[right], right))
                    used.remove(i)
                    used.add(right)
                    s += num + nums[right]

                        # Add the vacated element to the unused element heap
                    heappush(heap_unused, (-num, i))
                else:
                    # If the element being added to the window is larger than the largest used element, 
                    # place it on the unused element heap
                    heappush(heap_unused, (nums[right], right))

            if left >= 0:
                ans = min(s, ans)

        return nums[0] + ans
