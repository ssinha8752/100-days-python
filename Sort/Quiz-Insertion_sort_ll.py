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

    def insertion_sort(self):
        if self.head is None or self.head.next is None:
            return

        sorted_head = self.head
        current = self.head.next
        sorted_head.next = None

        while current:
            next_unsorted = current.next

            if current.value < sorted_head.value:
                # Insert at the beginning
                current.next = sorted_head
                sorted_head = current
            else:
                search = sorted_head
                while search.next and search.next.value < current.value:
                    search = search.next

                current.next = search.next
                search.next = current

            current = next_unsorted

        # Update head and tail
        self.head = sorted_head
        temp = self.head
        while temp.next:
            temp = temp.next
        self.tail = temp


my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.insertion_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""

