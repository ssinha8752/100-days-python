class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class ll:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1

    def show(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def pop(self):
        if self.length==0:
            return None
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        pre.next=None
        self.tail=pre
        self.length-=1
        if self.length==0:
            self.head=None
            self.tail=None
        return temp.value

    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1

    def pop_first(self):
        if self.length==0:
            return None
        temp=self.head
        self.head=self.head.next
        temp.next=None
        self.length-=1
        if self.length==0:
            self.tail=None
        return temp

my_ll=ll(1)
my_ll.append(2)
my_ll.append(4)
my_ll.prepend(500)
my_ll.show()
my_ll.pop_first()
my_ll.show()