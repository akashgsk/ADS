from simpleQueue import SimpleQueue

class StackusingQueue:

    def __init__(self):
        #Generate 2 Queues - q1 and q2
        self.q1=SimpleQueue()
        self.q2=SimpleQueue()

    #Enquing the element to Queue is same as Pushing the element to Stack
    def pushNew(self,ele):
        return self.q1.enqueue(ele)
    
    #Popping the element from stack should give top element but dequeue operation will give the rear element.
    #So dequeue element from Q1 and enqueue to Q2 until the last elemnt found.
    def popNew(self):
        while(self.q1.getElementCount()>1):
            self.q2.enqueue(self.q1.dequeue())
        ele=self.q1.dequeue()
        while(self.q2.getElementCount()>0):
            self.q1.enqueue(self.q2.dequeue())
        return ele
    
    def peekNew(self):
        while(self.q1.getElementCount()>1):
            self.q2.enqueue(self.q1.dequeue())
        ele=self.q1.peek()
        self.q2.enqueue(self.q1.dequeue())
        while(self.q2.getElementCount()>0):
            self.q1.enqueue(self.q2.dequeue())
        return ele
    
s1=StackusingQueue()
assert(s1.pushNew(16)==1)
assert(s1.pushNew(40)==2)
assert(s1.pushNew(55)==3)
assert(s1.popNew()==55)
assert(s1.peekNew()==40)