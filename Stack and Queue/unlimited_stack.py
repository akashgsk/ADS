class UnlimitedStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
   
stack = UnlimitedStack()

# Push elements onto the stack
stack.push(5)
stack.push(10)
stack.push(15)
stack.push(20)


# Pop elements from the stack
popped_item = stack.pop()
print("Popped:", popped_item)

# Peek at the top element
top_item = stack.peek()
print("Top item:", top_item)

# Check if the stack is empty
print("Is empty:", stack.is_empty())

# Get the size of the stack
print("Size:", stack.size())
