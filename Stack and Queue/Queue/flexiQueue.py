class FlexiQueue:

    defaultsize=2

    def __init__(self):
        self.data=[None]*FlexiQueue.defaultsize
        self.front=0
        self.count=0

    #Get the number of elements in the Queue
    def length(self):
        return self.count
    
    #Check if Queue is Empty
    def isEmpty(self):
        return self.count==0
    
    #Get first element in Queue
    def getFirst(self):
        if not self.isEmpty():
            return self.data[self.front]
        else:
            return None
        
    def enqueue(self, ele):
        #Checking if the queue is full
        #If its full Resize the Queue
        if self.count==len(self.data):
            self.resize(2*len(self.data))
        idx=(self.front+self.count)%len(self.data)
        self.data[idx]=ele
        self.count+=1
        return self.count
    
    def dequeue(self):
        if not self.isEmpty():
            ele=self.data[self.front]
            self.count-=1
            self.data[self.front]=None
            #Shrinking the queue size again, while deleting the element
            self.front=(self.front+1)%len(self.data)
            if 0<len(self.data)//4:
                self.resize(len(self.data)//2)
            return ele
        else:
            return None
        
    def resize(self,cap):
        oldData=self.data
        walk=self.front
        self.data=[None]*cap
        for k in range(self.count):
            self.data[k]=oldData[walk]
            walk=(walk+1)%len(oldData)
        self.front=0

    def getSize(self):
        return len(self.data)