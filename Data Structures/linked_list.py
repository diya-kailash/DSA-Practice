class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_start(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new
        
    def add_end(self, data):
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


