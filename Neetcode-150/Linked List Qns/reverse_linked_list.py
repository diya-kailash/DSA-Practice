# Reverse Linked List
# Overall Time Complexity: O(n)
# Overall Space Complexity: O(1)
# Hint: Traverse the list once, reverse pointers in-place

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    if head is None:
        return None
    prev = None
    current = head
    while current is not None:
        next_node = current.next 
        current.next = prev
        prev = current
        current = next_node
    return prev

# Time Complexity:
# - Traversing each node once: O(n)
# - Pointer reassignment: O(1) per node
# Space Complexity:
# - Constant space used for prev, current, and next_node: O(1)
# - No auxiliary data structures used
