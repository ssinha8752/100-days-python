class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Queue:

    def __init__(self,value):
        new_node=Node(value)
        self.bottom=new_node
        self.height=1

    def print_queue(self):
        temp=self.bottom
        while self.height>=1 and temp is not None:
            print(temp.value)
            temp=temp.next

Q=Queue(5)
Q.print_queue()


