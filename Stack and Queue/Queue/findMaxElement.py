from simpleQueue import SimpleQueue

class FindMaxElement:

    def __init__(self):
        #Initialize 2 Queues - q1 and q2
        self.q1=SimpleQueue()
        self.q2=SimpleQueue()

    #Print the elements in the Queue from Rear end to Front
    def printElements(self):
        return self.q1.printElements()
    
    #Find the Maximum element
    def findMax(self):
        self.max=0
        #We will dequeue every element from Queue & Compare it with a max.
        #If it more than max, Then max will be updated with the new value.
        while(self.q1.getElementCount()>0):
            ele=self.q1.dequeue()
            if(self.max<ele):
                self.max=ele
            self.q2.enqueue(ele)
        while(self.q2.getElementCount()>0):
            self.q1.enqueue(self.q2.dequeue())
        return self.max
    

s1=FindMaxElement()
assert(s1.q1.enqueue(90)==1)
assert(s1.q1.enqueue(10)==2)
assert(s1.q1.enqueue(85)==3)
assert(s1.findMax()==90)
assert(s1.q1.dequeue()==90)
assert(s1.findMax()==85)