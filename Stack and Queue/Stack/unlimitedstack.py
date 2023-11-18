class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class UnlimitedStack:

    def __init__(self):
        self.top = None

    def isStackEmpty(self):
        return self.top is None

    def getCount(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count

    def push(self, element):
        new_node = Node(element)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.isStackEmpty():
            popped = self.top.data
            self.top = self.top.next
            return popped
        else:
            return None

    def peek(self):
        if not self.isStackEmpty():
            return self.top.data
        else:
            return None

    def printElements(self):
        elements = []
        current = self.top
        while current:
            elements.append(current.data)
            current = current.next
        return elements
