from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers
        slow = head
        fast = head
        
        # Traverse the list
        while fast and fast.next:
            slow = slow.next          # Move slow pointer by 1
            fast = fast.next.next     # Move fast pointer by 2
            
            # If they meet, a cycle exists
            if slow == fast:
                return True
        
        # If fast pointer reaches the end, no cycle
        return False


# Example usage
if __name__ == "__main__":
    # Creating a linked list with a cycle for testing
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Creates a cycle
    
    sol = Solution()
    print(sol.hasCycle(node1))  # Output: True
