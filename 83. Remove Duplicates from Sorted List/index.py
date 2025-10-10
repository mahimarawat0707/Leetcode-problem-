from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head

def print_list(head: Optional[ListNode]):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))

solution = Solution()
new_head = solution.deleteDuplicates(head)

print("List after removing duplicates:")
print_list(new_head)
