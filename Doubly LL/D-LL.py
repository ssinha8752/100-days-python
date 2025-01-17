class Node:
    def __init__(self,val):
        self.value=val
        self.next=None
        self.prev=None


class DoublyLinkedList:
    def __init__(self,val):
        new_node=Node(val)
        self.head=new_node
        self.tail=new_node
        self.length=1


    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

my_dll=DoublyLinkedList(7)
my_dll.print_list()