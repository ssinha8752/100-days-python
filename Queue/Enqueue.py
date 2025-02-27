class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Queue:

    def __init__(self,value):
        new_node=Node(value)
        self.top=new_node
        self.bottom=new_node
        self.height=1

    def print_queue(self):
        temp=self.top
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def enqueue(self,value):
        new_node=Node(value)
        if self.top is None:
            self.top=new_node
            self.bottom=new_node
        else:
            self.bottom.next=new_node
            self.bottom=new_node
        self.height+=1


Q=Queue(5)
Q.print_queue()
Q.enqueue(6)
Q.print_queue()


