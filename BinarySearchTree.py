class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if data < self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def search(self, data):
        if self.key == data:
            print("Node is present in the BST")
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present in the Tree")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present in the Tree")

    def preorder(self):
        print(self.key, end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key, end=" ")
        if self.rchild:
            self.rchild.inorder()

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key, end=" ")

    def delete(self, data, curr):
        if self.key is None:
            print("Tree is empty")
            return None
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data, curr)
            else:
                print("Given node is not present in the tree")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data, curr)
            else:
                print("Given node is not present in the tree")
        else:
            # Node with only one child or no child
            if self.lchild is None:
                temp = self.rchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return None
                self = None
                return temp
            elif self.rchild is None:
                temp = self.lchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return None
                self = None
                return temp

            # Node with two children: get the inorder successor
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key, curr)

        return self

def count(node):
    if node is None:
        return 0
    return 1 + count(node.lchild) + count(node.rchild)

root = BST(10)
list1 = [6, 3]
for i in list1:
    root.insert(i)

print("Node count:", count(root))
print("Preorder Tree:")
root.preorder()
print()

if count(root) > 1:
    root.delete(6, root.key)
else:
    print("Can't delete")

print("Preorder after deleting 6:")
root.preorder()
print()

print("Inorder Tree")
root.inorder()
print()

print("Postorder")
root.postorder()
print()

root.delete(10, root.key)
print("Preorder after deleting root (10):")
root.preorder()
