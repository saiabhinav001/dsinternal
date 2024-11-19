# Stack using LinkedList

class Node:
    def __init__(self, data):
        self.data = data  # Stores the actual value
        self.next = None  # Points to the next node, initially None

class Stack:
    def __init__(self):
        self.top = None  # Initializes an empty stack with top pointing to None

    def is_empty(self):
        return self.top is None  # Returns True if stack is empty, False otherwise

    def push(self, data):
        new_node = Node(data)  # Create new node
        new_node.next = self.top  # New node points to current top
        self.top = new_node  # New node becomes the top

    def pop(self):
        if self.is_empty():
            return None
        n = self.top  # Store current top
        self.top = self.top.next  # Move top to next node
        return n.data  # Return popped value

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data  # Returns top element without removing it

    def display(self):
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

my_stack = Stack()
my_stack.push(10)  # Stack: 10
my_stack.push(20)  # Stack: 20 -> 10
my_stack.push(5)   # Stack: 5 -> 20 -> 10
my_stack.push(30)  # Stack: 30 -> 5 -> 20 -> 10
my_stack.display() # Prints: 30 -> 5 -> 20 -> 10 -> None
print(f"Popped item: {my_stack.pop()}")  # Removes and prints 30
print(f"Popped item: {my_stack.pop()}")  # Removes and prints 5
print(f"Peek element: {my_stack.peek()}") # Shows top element (20) without removing it
my_stack.display() # Prints: 20 -> 10 -> None
