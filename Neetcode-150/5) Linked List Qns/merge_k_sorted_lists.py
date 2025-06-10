# Merge K Sorted Lists
# Overall Time Complexity: O(n * k)
# Overall Space Complexity: O(1)
# Hint: Sequentially merge 2 lists at a time

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_list(l1, l2):
   current = dummy = ListNode(0)
   while l1 and l2:
       if l1.val < l2.val:
           current.next = l1
           l1 = l1.next
       else:
           current.next = l2
           l2 = l2.next
       current = current.next
   if l1:
       current.next = l1
   if l2:
       current.next = l2
   return dummy.next

def mergeKLists(lists):
   if not lists:
       return None
   for i in range(1, len(lists)):
       lists[i] = merge_list(lists[i], lists[i-1])
   return lists[-1]

# Time Complexity:
# - mergeKLists(): O(n * k) where n is average list length, k is number of lists
# - First merge: O(n), second merge: O(2n), third merge: O(3n), ..., kth merge: O(kn)
# Space Complexity:
# - merge_list(): O(1) - only uses dummy node and pointers, reuses existing nodes
# - mergeKLists(): O(1) - modifies input array in-place, no additional space
# - Overall: O(1) - constant extra space excluding input/output