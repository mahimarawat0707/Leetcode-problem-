from typing import Optional
from heapq import heappush, heappop

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        heap = []

        # Push all values into the heap
        while head:
            heappush(heap, head.val)
            head = head.next

        # Dummy node for the sorted list
        dummy = ListNode(0)
        curr = dummy

        # Pop from heap and rebuild linked list
        while heap:
            curr.next = ListNode(heappop(heap))
            curr = curr.next

        return dummy.next
