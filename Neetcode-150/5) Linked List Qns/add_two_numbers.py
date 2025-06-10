# Add Two Numbers 
# Overall Time Complexity: O(max(n, m))
# Overall Space Complexity: O(1)
# Hint: Simulate addition with carry, create new nodes for result

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
   current = dummy = ListNode(0)  
   carry = 0  
   while l1 or l2:  
       val1 = l1.val if l1 else 0  
       val2 = l2.val if l2 else 0  
       add = val1 + val2 + carry  
       carry = add // 10  
       current.next = ListNode(add % 10)  
       current = current.next  
       if l1: l1 = l1.next  
       if l2: l2 = l2.next  
   if carry:  
       current.next = ListNode(carry)  
   return dummy.next  

# Time Complexity:
# - Main while loop runs max(n, m) times where n = length of l1, m = length of l2: O(max(n, m))
# - Each iteration performs constant time operations: O(1) per iteration
# - Final carry check: O(1)
# Space Complexity:
# - Constant space for variables (dummy, current, carry, val1, val2, add): O(1)
# - Space used for the new linked list creation, i.e. the output list: O(max(n, m))