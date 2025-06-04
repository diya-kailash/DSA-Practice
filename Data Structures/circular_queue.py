class CircularQueue:
    def __init__(self, max_size=10):
        self.items = [None] * max_size
        self.front = -1
        self.rear = -1
        self.max_size = max_size

    def is_empty(self):
        return self.front == -1 and self.rear == -1

    def is_full(self):
        return (self.rear + 1) % self.max_size == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Queue is Full")
            return
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.max_size
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
            self.front = (self.front + 1) % self.max_size
        return item

    def size(self):
        if self.is_empty():
            return 0
        elif self.rear >= self.front:
            return self.rear - self.front + 1
        else:
            return self.max_size - self.front + self.rear + 1

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("Queue elements:")
        i = self.front
        while i != self.rear:
            print(self.items[i])
            i = (i + 1) % self.max_size
        print(self.items[self.rear])

# Example usage
queue = CircularQueue(5)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.display()
print("Size after enqueue 40:", queue.size())  # 4
queue.enqueue(50)
queue.enqueue(60)
print("Dequeued:", queue.dequeue())  # 10
print("Dequeued:", queue.dequeue())  # 20
queue.display()
print("Size after 2nd dequeue:", queue.size())  # 3
queue.enqueue(70)
queue.display()
print("Size after enqueue 70:", queue.size())  # 5

