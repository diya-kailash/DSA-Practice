# LRU Cache 
# Overall Time Complexity: O(1) for both get and put operations
# Overall Space Complexity: O(n) where n is the capacity of the cache
# Hint: Use hashmap + doubly linked list for O(1) operations

class Node:
   def __init__(self, key, val):
       self.key, self.val = key, val
       self.prev = self.next = None

class LRUCache:
   def __init__(self, capacity: int):
       self.capacity = capacity
       self.items = {} 
       # LEFT POINTS TO LRU RIGHT POINTS TO MRU
       self.left, self.right = Node(0, 0), Node(0, 0)    
       self.left.next, self.right.prev = self.right, self.left 

   # REMOVE NODE FROM LIST
   def remove(self, node):
       prv, nxt = node.prev, node.next
       prv.next, nxt.prev = nxt, prv

   # INSERT NODE AT RIGHT I.E. MAKE IT MRU
   def insert(self, node):
       prv, nxt = self.right.prev, self.right
       prv.next = nxt.prev = node
       node.next, node.prev = nxt, prv

   def get(self, key: int) -> int:
       if key in self.items:
           self.remove(self.items[key])
           self.insert(self.items[key])
           return self.items[key].val
       return -1       

   def put(self, key: int, value: int) -> None:
       if key in self.items:
           self.remove(self.items[key])
       self.items[key] = Node(key, value)
       self.insert(self.items[key])
       if len(self.items) > self.capacity:
           lru = self.left.next
           self.remove(lru)
           del self.items[lru.key]

# Time Complexity:
# - get(): O(1) - hashmap lookup, remove, and insert operations are all O(1)
# - put(): O(1) - hashmap operations, node creation, remove, insert are all O(1)
# - remove(): O(1) - updating pointer references in doubly linked list
# - insert(): O(1) - updating pointer references in doubly linked list
# Space Complexity:
# - O(n) - hashmap stores at most 'capacity' key-value pairs
# - O(n) - doubly linked list stores at most 'capacity' nodes
# - O(1) - dummy nodes (left, right) use constant space
# Overall, the space complexity is O(n) where n is the capacity of the cache.