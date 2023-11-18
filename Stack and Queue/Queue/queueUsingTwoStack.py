from stack import Stack

class QueueusingStack:
    def __init__(self):
        #GEnerate 2 stacks - s1 and s2
        self.s1=Stack()
        self.s2=Stack()

    def enqueueNew(self,ele):
        #Enquing to Queue is same as Pushing the elemnt to Stack
        self.s1.push(ele)
        return self.s1.count
    
    def dequeueNew(self):
        #To dequeue an element we need to get the rear element but in stack we can have only top element
        #Pop element from stack until we find the last element and push it to new stack S2. 
        #The last element from S1 popped will be the front element. #
        #Then again from S2 pop element to s1.
        while(self.s1.getCount()>1):
            self.s2.push(self.s1.pop())
        ele=self.s1.pop()
        while(self.s2.getCount()>0):
            self.s1.push(self.s2.pop())
        return ele
    
    def peekNew(self):
        while(self.s1.getCount()>1):
            self.s2.push(self.s1.pop())
        ele=self.s1.peek()
        self.s2.push(self.s1.pop())
        while(self.s2.getCount()>0):
            self.s1.push(self.s2.pop())
        return ele
    

q1=QueueusingStack()
assert(q1.enqueueNew(11)==1)
assert(q1.enqueueNew(22)==2)
assert(q1.enqueueNew(33)==3)
assert(q1.dequeueNew()==11)
assert(q1.peekNew()==22)