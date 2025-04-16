class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None


class BST:
    def __init__(self):
        self.root=None

my_tree=BST()

print(my_tree.root)