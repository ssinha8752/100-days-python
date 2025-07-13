class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def merge(self, other_list):
        dummy = Node(0)
        tail = dummy
        p1 = self.head
        p2 = other_list.head

        while p1 and p2:
            if p1.value < p2.value:
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p2
                p2 = p2.next
            tail = tail.next

        # Attach any remaining nodes
        tail.next = p1 if p1 else p2

        # Update self.head
        self.head = dummy.next

        # Update self.tail safely
        if self.head is None:
            self.tail = None
            self.length = 0
        else:
            temp = self.head
            self.length = 1
            while temp.next:
                temp = temp.next
                self.length += 1
            self.tail = temp


l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)

l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)

l1.merge(l2)

l1.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    1 
    2 
    3 
    4 
    5 
    6 
    7
    8

"""