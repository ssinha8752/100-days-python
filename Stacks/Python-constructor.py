class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Stack:



my_stack = Stack(4)

print('Top:', my_stack.top.value)
print('Height:', my_stack.height)

"""
    EXPECTED OUTPUT:
    ----------------
    Top: 4
    Height: 1

"""