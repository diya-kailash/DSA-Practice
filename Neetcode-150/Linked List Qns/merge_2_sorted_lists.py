# Merge Two Sorted Linked Lists
# Overall Time Complexity: O(n + m)
# Overall Space Complexity: O(1)
# Hint: Use two pointers to compare and merge nodes into a dummy list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    dummy = ListNode()
    current = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    if list1:
        current.next = list1
    if list2:
        current.next = list2
    return dummy.next

# Time Complexity:
# - Comparing and appending each node from list1 and list2: O(n + m)
# - n = length of list1, m = length of list2
# Space Complexity:
# - Only constant space used for dummy and current pointers: O(1)
# - No new nodes are created; links are reused
