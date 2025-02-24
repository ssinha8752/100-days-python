class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class Stack:
    def __init__(self,val):
        new_node=Node(val)
        self.top=new_node
        self.height=1

    def print_stack(self):
        temp=self.top
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def push(self,val):
        new_node=Node(val)
        if self.height==0:
            self.top=new_node
        else:
            new_node.next=self.top
            self.top=new_node
        self.height+=1

my_stack=Stack(5)
my_stack.push(6)
my_stack.print_stack()