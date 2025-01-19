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

    def append(self, value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1
        return True

my_dll=DoublyLinkedList(7)
my_dll.append(8)
my_dll.print_list()