class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def insert_start(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new
        
    def insert_end(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new

    def insert_at(self, data, pos):
        if pos <= 0 or pos > self.size() + 1:
            print("Invalid position")
            return
        new = Node(data)
        if pos == 1:
            self.insert_start(data)
        elif pos == self.size() + 1:
            self.insert_end(data)
        else:
            current = self.head
            for i in range(pos - 2):
                current = current.next
            new.next = current.next
            current.next = new

    def delete_start(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        return temp

    def delete_end(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            temp = self.head
            self.head = None
            return temp
        current = self.head
        while current.next.next is not None:
            current = current.next
        temp = current.next
        current.next = None
        return temp
    
    def delete_at(self, pos):
        if pos <= 0 or pos > self.size():
            print("Invalid position")
            return
        if pos == 1:
            return self.delete_start()
        elif pos == self.size():
            return self.delete_end()
        else:
            current = self.head
            for i in range(pos - 2):
                current = current.next
            temp = current.next
            current.next = temp.next if temp else None
            return temp
    
    def delete_value(self, data):
        if self.head is None:
            return None
        if self.head.data == data:
            return self.delete_start()
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                temp = current.next
                current.next = temp.next
                return temp
            current = current.next
        return None 

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while current is not None:
            print(current.data, end=" -> " if current.next else "\n")
            current = current.next

    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

# Example usage of LinkedList class
ll = LinkedList()

print("Inserting at start:")
ll.insert_start(10)
ll.insert_start(20)
ll.display()

print("\nInserting at end:")
ll.insert_end(30)
ll.insert_end(40)
ll.display()

print("\nInserting at position:")
ll.insert_at(25, 3)  
ll.display()
ll.insert_at(5, 1)  
ll.display()
ll.insert_at(50, ll.size() + 1)  
ll.display()

print("\nDeleting from start:")
deleted_node = ll.delete_start()
print(f"Deleted: {deleted_node.data}")
ll.display()

print("\nDeleting from end:")
deleted_node = ll.delete_end()
print(f"Deleted: {deleted_node.data}")
ll.display()

print("\nDeleting from specific position:")
deleted_node = ll.delete_at(3)
print(f"Deleted: {deleted_node.data}")
ll.display()

print("\nDeleting by value:")
deleted_node = ll.delete_value(25)
print(f"Deleted: {deleted_node.data if deleted_node else 'Value not found'}")
ll.display()

print("\nSearching for values:")
print("Is 30 in list?", ll.search(30))
print("Is 99 in list?", ll.search(99))

print("\nCurrent size of the list:")
print("Size:", ll.size())

print("\nReversing the list:")
ll.reverse()
ll.display()
