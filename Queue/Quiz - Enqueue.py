class MyQueue:
    def __init__(self):
        self.stack1 = []  # Main stack to store elements
        self.stack2 = []  # Temporary stack for reordering

    def enqueue(self, value):
        # Step 1: Transfer elements from stack1 to stack2
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        # Step 2: Add the new value to stack1
        self.stack1.append(value)

        # Step 3: Transfer elements back from stack2 to stack1
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def peek(self):
        # Return the element at the front of the queue (last element in stack1)
        return self.stack1[-1] if self.stack1 else None

    def is_empty(self):
        # Check if stack1 is empty
        return len(self.stack1) == 0


# Create a new queue
q = MyQueue()

# Enqueue some values
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Output the front of the queue
print("Front of the queue:", q.peek())  # Expected Output: 1

# Check if the queue is empty
print("Is the queue empty?", q.is_empty())  # Expected Output: False