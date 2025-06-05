# Linked List Cycle Detection (Floyd's Tortoise and Hare)
# Overall Time Complexity: O(n)
# Overall Space Complexity: O(1)
# Hint: Use slow and fast pointers - moving at different speeds; if there's a cycle, they will eventually meet

def hasCycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Time Complexity:
# - Each pointer moves at most n steps: O(n)
# - In worst case, fast catches up with slow in a cycle after O(n) steps
# Space Complexity:
# - Only two pointers (slow and fast) used: O(1)
# - No additional data structures
