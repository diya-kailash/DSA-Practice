class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

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
    
    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count
    
    # def reverse(self):
    # def insert_at(self, data, position):
    # def delete_at(self, position):
    # def delete_value(self, data):


