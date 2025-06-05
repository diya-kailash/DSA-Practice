# Reorder Linked List (L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …)
# Overall Time Complexity: O(n)
# Overall Space Complexity: O(1)
# Hint: Use fast and slow pointer to find middle, reverse second half, then merge two halves

def reverse(head):
    prev = None 
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def reorderList(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    first = head
    second = reverse(slow.next)
    slow.next = None
    while second:
        tmp1, tmp2 = first.next, second.next 
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2

# Time Complexity:
# - Finding the middle using slow/fast pointers: O(n)
# - Reversing second half of the list: O(n)
# - Merging two halves: O(n)
# Space Complexity:
# - Only a few pointers used (slow, fast, first, second, tmp1, tmp2): O(1)
# - No extra data structures used