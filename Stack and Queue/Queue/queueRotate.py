from simpleQueue import SimpleQueue
from stack import Stack


class Rotate:

    #Use Stack to Rotate contents of Queue
    def __init__(self):
        self.q1=SimpleQueue()
        self.s1=Stack()

    def rotateMethodUsingStack(self):
        while(self.q1.count>0):
            self.s1.push(self.q1.dequeue())
        while(self.s1.count>0):
            self.q1.enqueue(self.s1.pop())
        return self.q1.printElements()

q=Rotate()
q.q1.enqueue(11)
q.q1.enqueue(22)
q.q1.enqueue(33)
q.q1.enqueue(44)
assert(q.rotateMethodUsingStack()==([44,33,22,11]))