# FIXED SIZE QUEUE
class Queue:
    def __init__(self, max_size=10):
        self.items = [None] * max_size
        self.front = -1
        self.rear = -1
        self.max_size = max_size

    def is_empty(self):
        return self.front == -1 and self.rear == -1

    def is_full(self):
        return self.rear == self.max_size - 1

    def enqueue(self, item):
        if self.is_full():
            print("Queue is Full")
            return
        if self.is_empty():
            self.front = 0
        self.rear += 1
        self.items[self.rear] = item
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
            return None
        item = self.items[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front += 1
        return item

    def size(self):
        return self.rear - self.front + 1 if not self.is_empty() else 0

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("Queue elements:")
        for i in range(self.front, self.rear + 1):
            print(self.items[i])

# Example usage
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()
queue.dequeue()
queue.dequeue()
queue.display()
queue.enqueue(40)
queue.display()
print(queue.size())