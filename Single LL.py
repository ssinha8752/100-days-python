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


my_ll=ll(1)
my_ll.append(2)
my_ll.append(4)
my_ll.show()
my_ll.pop()
my_ll.pop()
my_ll.pop()
print(my_ll.pop())
my_ll.show()