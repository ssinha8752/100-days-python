class Node:
    def __init__(self, value):
        self.left=None
        self.right=None
        self.value=value

class BinarySearchTree:

    def __init__(self):
        self.root=None


my_tree = BinarySearchTree()

print("Root:", my_tree.root)