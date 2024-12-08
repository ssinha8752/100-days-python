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


my_ll=ll(1)
my_ll.append(2)
my_ll.show()
my_ll.append(4)