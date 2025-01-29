class Node:
    def __init__(self,val):
        self.next=None
        self.prev=None
        self.value=val

class DoublyLinkedList:

    def __init__(self,val):
        new_Node=Node(val)
        self.head=new_Node
        self.tail=new_Node
        self.length=1

my_doubly_linked_list = DoublyLinkedList(7)

print('Head:', my_doubly_linked_list.head.value)
print('Tail:', my_doubly_linked_list.tail.value)
print('Length:', my_doubly_linked_list.length)

"""
    EXPECTED OUTPUT:
    ----------------
    Head: 7
    Tail: 7
    Length: 1

"""
