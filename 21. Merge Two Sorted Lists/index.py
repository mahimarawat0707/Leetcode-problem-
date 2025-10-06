from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Merge two sorted linked lists and return the head of the new sorted list.
        Both list1 and list2 are sorted in ascending order.
        """
        
        dummy = ListNode()
        current = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        current.next = list1 if list1 else list2
        
        return dummy.next

if __name__ == "__main__":
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))

    solution = Solution()
    merged = solution.mergeTwoLists(l1, l2)

    while merged:
        print(merged.val, end=" -> ")
        merged = merged.next
    print("None")
