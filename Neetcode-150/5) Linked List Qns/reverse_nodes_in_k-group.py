# Reverse Nodes in K-Group
# Overall Time Complexity: O(n)
# Overall Space Complexity: O(1)
# Hint: Find k-th node, reverse group, reconnect with previous and next groups

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getKth(self, current, k):
    while current and k > 0:
        current = current.next
        k-=1
    return current
       
def reverseKGroup(head, k):
    dummy = ListNode(0, head)
    group_prev = dummy
    while True:
        kth = getKth(group_prev, k)
        if not kth:
            break
        group_next = kth.next

        prev = group_next
        current = group_prev.next
        while current != group_next:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        temp = group_prev.next
        group_prev.next = kth
        group_prev = temp
    return dummy.next

# Time Complexity:
# - getKth(): O(k) - traverses at most k nodes to find k-th node
# - Main while loop: O(n/k) iterations where n is total number of nodes
# - Each iteration: O(k) for getKth() + O(k) for reversing k nodes
# - Total: O(n/k * k) = O(n) - each node is visited exactly twice
# Space Complexity:
# - O(1) - only uses constant extra space for pointers (dummy, group_prev, kth, etc.)
# - No recursion or additional data structures used
# - Reversal done in-place by modifying existing node connections