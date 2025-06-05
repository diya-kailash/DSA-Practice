# Copy List with Random Pointer
# Overall Time Complexity: O(n)
# Overall Space Complexity: O(n)
# Hint: First pass creates node copies and maps them; second pass assigns random pointers

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head):
    node = dummy = Node(0)
    hashmap = {}
    current = head
    while current:
        node.next = Node(current.val)
        hashmap[current] = node.next
        node = node.next
        current = current.next
    current = head
    node = dummy.next
    while current:
        if current.random:
            node.random = hashmap[current.random]
        node = node.next
        current = current.next
    return dummy.next

# Time Complexity:
# - First pass (copy nodes and build hashmap): O(n)
# - Second pass (assign random pointers): O(n)
# Space Complexity:
# - HashMap to store original -> copy mapping: O(n)
# - Other variables use constant space
