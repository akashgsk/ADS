class LimitedStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = []

    def push(self, item):
        if len(self.stack) < self.max_size:
            self.stack.append(item)
        else:
            print("Stack is full. Cannot push item:", item)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print("Stack is empty.")
            return None

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            print("Stack is empty.")
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.max_size

    def size(self):
        return len(self.stack)

    def print_stack(self):
        print("Stack elements:", self.stack)

# Create a limited-size stack with max size of 3
stack = LimitedStack(max_size=3)

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)  # This will print "Stack is full. Cannot push item: 4"

stack.print_stack()  # Output: Stack elements: [1, 2, 3]
class LimitedStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = []

    def push(self, item):
        if len(self.stack) < self.max_size:
            self.stack.append(item)
        else:
            print("Stack is full. Cannot push item:", item)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print("Stack is empty.")
            return None

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            print("Stack is empty.")
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.max_size

    def size(self):
        return len(self.stack)

    def print_stack(self):
        print("Stack elements:", self.stack)

# Create a limited-size stack with max size of 3
stack = LimitedStack(max_size=3)

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)  # This will print "Stack is full. Cannot push item: 4"

stack.print_stack()  # Output: Stack elements: [1, 2, 3]

print(stack.pop())  # Output: 3
print(stack.peek())  # Output: 2
print(stack.size())  # Output: 1

stack.print_stack()  # Output: Stack elements: [1, 2]
class LimitedStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = []

    def push(self, item):
        if len(self.stack) < self.max_size:
            self.stack.append(item)
        else:
            print("Stack is full. Cannot push item:", item)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print("Stack is empty.")
            return None

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            print("Stack is empty.")
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.max_size

    def size(self):
        return len(self.stack)

    def print_stack(self):
        print("Stack elements:", self.stack)

# Create a limited-size stack with max size of 3
stack = LimitedStack(max_size=3)

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)  # This will print "Stack is full. Cannot push item: 4"

stack.print_stack()  # Output: Stack elements: [1, 2, 3]



stack.print_stack()  # Output: Stack elements: [1, 2]

print("Popped Element :")
print(stack.pop())  # Output: 3
print("Peak Element :")
print(stack.peek())  # Output: 2
print("Stack Size :")
print(stack.size())  # Output: 1

stack.print_stack()  # Output: Stack elements: [1, 2]
