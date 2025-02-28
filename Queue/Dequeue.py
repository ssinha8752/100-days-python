class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.bottom = new_node
        self.height = 1

    def enqueue(self, value):
        new_node = Node(value)
        if self.top is None:  # Queue is empty
            self.top = new_node
            self.bottom = new_node
        else:
            self.bottom.next = new_node
            self.bottom = new_node
        self.height += 1

    def dequeue(self):
        if self.top is None:  # Queue is empty
            return None
        temp = self.top
        if self.height == 1:  # Only one element in the queue
            self.top = None
            self.bottom = None
        else:
            self.top = self.top.next
        self.height -= 1
        return temp.value

    def print_queue(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next


# Test the Queue
Q = Queue(5)
Q.enqueue(1)
Q.enqueue(2)
Q.print_queue()

print(Q.dequeue())  # Should print 5 (the first value added)
print(Q.dequeue())  # Should print 1 (the next value added)
