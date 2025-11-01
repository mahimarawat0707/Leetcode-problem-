# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums, head):
        remove_set = set(nums)
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy

        while curr.next:
            if curr.next.val in remove_set:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next


# ----------------------------
# Helper functions for testing
# ----------------------------

# Create linked list from Python list
def build_linked_list(values):
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

# Convert linked list back to Python list for easy display
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# ----------------------------
# Example test cases
# ----------------------------

if __name__ == "__main__":
    sol = Solution()

    # Example 1
    nums = [1, 2, 3]
    head = build_linked_list([1, 2, 3, 4, 5])
    new_head = sol.modifiedList(nums, head)
    print("Example 1 Output:", linked_list_to_list(new_head))  # [4, 5]

    # Example 2
    nums = [1]
    head = build_linked_list([1, 2, 1, 2, 1, 2])
    new_head = sol.modifiedList(nums, head)
    print("Example 2 Output:", linked_list_to_list(new_head))  # [2, 2, 2]

    # Example 3
    nums = [5]
    head = build_linked_list([1, 2, 3, 4])
    new_head = sol.modifiedList(nums, head)
    print("Example 3 Output:", linked_list_to_list(new_head))  # [1, 2, 3, 4]
