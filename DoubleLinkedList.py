class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def printLL(self):
        if self.head is None:
            print("List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, end=" <--> ")
                n = n.next
            print("None")

    def printLL_reverse(self):
        if self.head is None:
            print("List is empty")
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            while n is not None:
                print(n.data, end=" <--> ")
                n = n.prev
            print("None")

    def add_begin(self,item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_end(self,item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
            new_node.prev = n

    def add_before(self,item,x):
        if self.head is None:
            print("List is empty")
            return

        elif self.head.data == x:
            self.add_begin(item)
            return

        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.next
            if n is None:
                print("Node not found")
            else:
                new_node = Node(item)
                new_node.prev = n.prev
                new_node.next = n
                if n.prev is not None:
                    n.prev.next = new_node
                n.prev = new_node

    def add_after(self,item,x):
        if self.head is None:
            print("List is empty")
            return
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.next
        if n is None:
            print("Node is not found")
        else:
            new_node = Node(item)
            new_node.next = n.next
            new_node.prev = n
            if n.next is not None:
                n.next.prev = new_node
            n.next = new_node

    def delete_begin(self):
        if self.head is None:
            print("List is empty")
        else:
            if self.head.next is None:
                self.head = None
            else:
                self.head = self.head.next
                self.head.prev = None

    def delete_end(self):
        if self.head is None:
            print("List is empty")
        else:
            if self.head.next is None:
                self.head = None
            else:
                n = self.head
                while n.next is not None:
                    n = n.next
                n.prev.next = None

    def delete_value(self,x):
        if self.head is None:
            print("List is empty")
        else:
            if self.head.data == x:
                self.delete_begin()
                return
            else:
                n = self.head
                while n is not None:
                    if n.data == x:
                        break
                    n = n.next
                if n is None:
                    print("Node is not found")
                else:
                    if n.next is not None:
                        n.next.prev = n.prev
                    if n.prev is not None:
                        n.prev.next = n.next

DLL = DoubleLinkedList()
DLL.add_begin(20)
DLL.add_begin(10)
DLL.printLL()
DLL.add_end(30)
DLL.printLL()
DLL.add_before(15,20)
DLL.printLL()
DLL.add_after(25,20)
DLL.printLL()
DLL.delete_begin()
DLL.printLL()
DLL.delete_end()
DLL.printLL()
DLL.delete_value(15)
DLL.printLL()
DLL.printLL_reverse()
