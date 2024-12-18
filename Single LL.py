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

    def get(self,index):
        if index<0 or index>=self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp=temp.next
            return temp

    def set_value(self, index, val):
        if index<0 or index>self.length:
            return None
        else:
            temp=self.head
            for _ in range(index):
                temp=temp.next
            temp.value=val
            return True

    def set_value1(self,index,val):
        temp=self.get(index)
        if temp:
            temp.value=val
            return True
        return False

    def insert(self, index, val):
        node=Node(val)
        if index<0 or index>self.length:
            return None
        if index==0:
            return self.prepend(val)
        if index==self.length:
            return self.append(val)
        temp=self.get(index-1)
        node.next=temp.next
        temp.next=node
        self.length+=1
        return True

    def remove(self,index):
        if index<self.length<0 or index>=self.length:
            return None
        if index==0:
            self.pop_first()
        if index==self.length-1:
            self.pop()
        prev=self.get(index-1)
        temp=prev.next
        prev.next=temp.next
        temp.next=None
        self.length-=1
        return temp


my_ll=ll(1)
my_ll.append(2)
my_ll.append(4)
my_ll.prepend(500)
my_ll.show()
print(my_ll.get(0))
print(my_ll.set_value(0,10))
my_ll.insert(2,999)
my_ll.show()