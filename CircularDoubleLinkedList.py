class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class CircularDoubleLinkedList:
    def __init__(self):
        self.head = None

    def printLL(self):
        if self.head is None:
            print("List is empty")
        else:
            n = self.head
            while True:
                print(n.data, "<-->", end=" ")
                n = n.next
                if n == self.head:
                    break
            print("HEAD")

    def printLL_reverse(self):
        if self.head is None:
            print("List is empty")
        else:
            n = self.head
            while n.next != self.head:  # Move to the last node
                n = n.next
            last = n
            while True:
                print(n.data, "<-->", end=" ")
                n = n.prev
                if n == last:
                    break
            print("HEAD")

    def add_begin(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            last = self.head.prev
            new_node.next = self.head
            new_node.prev = last
            last.next = new_node
            self.head.prev = new_node
            self.head = new_node

    def add_end(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            last = self.head.prev
            last.next = new_node
            new_node.prev = last
            new_node.next = self.head
            self.head.prev = new_node

    def add_before(self, item, x):
        if self.head is None:
            print("List is empty")
            return
        n = self.head
        while True:
            if n.data == x:
                break
            n = n.next
            if n == self.head:
                print("Node not found")
                return
        new_node = Node(item)
        new_node.next = n
        new_node.prev = n.prev
        n.prev.next = new_node
        n.prev = new_node
        if n == self.head:  # Update head if needed
            self.head = new_node

    def add_after(self, item, x):
        if self.head is None:
            print("List is empty")
            return
        n = self.head
        while True:
            if n.data == x:
                break
            n = n.next
            if n == self.head:
                print("Node not found")
                return
        new_node = Node(item)
        new_node.prev = n
        new_node.next = n.next
        n.next.prev = new_node
        n.next = new_node

    def delete_begin(self):
        if self.head is None:
            print("List is empty")
        elif self.head.next == self.head:  # Single node case
            self.head = None
        else:
            last = self.head.prev
            self.head = self.head.next
            self.head.prev = last
            last.next = self.head

    def delete_end(self):
        if self.head is None:
            print("List is empty")
        elif self.head.next == self.head:  # Single node case
            self.head = None
        else:
            last = self.head.prev
            second_last = last.prev
            second_last.next = self.head
            self.head.prev = second_last

    def delete_value(self, x):
        if self.head is None:
            print("List is empty")
            return
        n = self.head
        while True:
            if n.data == x:
                break
            n = n.next
            if n == self.head:
                print("Node not found")
                return
        if n.next == n:  # Single node case
            self.head = None
        else:
            n.prev.next = n.next
            n.next.prev = n.prev
            if n == self.head:  # Update head if needed
                self.head = n.next


CDLL = CircularDoubleLinkedList()
CDLL.add_begin(10)
CDLL.printLL()
CDLL.add_begin(20)
CDLL.printLL()
CDLL.add_begin(30)
CDLL.printLL()
CDLL.add_end(40)
CDLL.printLL()
CDLL.add_before(5, 40)
CDLL.printLL()
CDLL.add_after(31, 10)
CDLL.printLL()
CDLL.add_after(10, 30)
CDLL.printLL()
CDLL.delete_begin()
CDLL.printLL()
CDLL.delete_end()
CDLL.printLL()
CDLL.delete_value(10)

CDLL.printLL()
CDLL.printLL_reverse()