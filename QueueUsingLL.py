# Queue Using LinkedList

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp.data

    def peek(self):
        if self.front is None:
            return None
        return self.front.data

    def display(self):
        n = self.front
        while n:
            print(n.data, end=' ')
            n = n.next
        print()

my_queue = Queue()
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)
my_queue.enqueue(40)
my_queue.display()
print(f"Dequeued element is: {my_queue.dequeue()}")
print(f"Dequeued element is: {my_queue.dequeue()}")
my_queue.dequeue()
print(f"Front element is: {my_queue.peek()}")
