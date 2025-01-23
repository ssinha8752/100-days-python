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

    def pop(self):
        if self.length==0:
            return None
        temp=self.tail
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.tail=temp.prev
            self.tail.next=None
            temp.prev=None
        self.length-=1
        return temp

    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.head.prev=new_node
            new_node.next=self.head
            self.head=new_node
        self.length+=1
        return True

    def pop_first(self):
        if self.length==0:
            return None
        temp=self.head
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head=temp.next
            self.head.prev=None
            temp.next=None
        self.length-=1
        return True


my_dll=DoublyLinkedList(7)
my_dll.append(8)
my_dll.append(9)
my_dll.pop()
my_dll.prepend(3)
my_dll.pop_first()
my_dll.print_list()