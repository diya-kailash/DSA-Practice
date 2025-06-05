# Remove nth Node From End of Linked List
# Overall Time Complexity: O(N)
# Overall Space Complexity: O(1)
# Hint: Remove the (N - n)th node from the start

def size(head):
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    return length 

def removeNthFromEnd(head, n):
    N = size(head)
    pos = N - n
    if pos == 0:
        return head.next
    current = head
    for i in range(pos - 1):
        current = current.next
    current.next = current.next.next
    return head

# Time Complexity:
# - Calculating size of list: O(N)
# - Traversing to (N - n)-th node: O(N)
# - Total: O(N) where N is the number of nodes in the list
# Space Complexity:
# - Only a few pointers/integers used (current, length, pos): O(1)
# - No additional data structures
