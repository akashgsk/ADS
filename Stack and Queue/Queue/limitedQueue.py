class LimitedQueue:

    def __init__(self):
        self.count=0
        #Defining size of the queue[limited]
        self.data=[None]*5
        self.front=-1

    #Checking if queue is full
    def isQueueFull(self):
        return self.count>=len(self.data)
    
    #Checking if queue is Empty
    def isQueueEmpty(self):
        return self.count==0 
    
    #Count of elements in queue
    def getCount(self):
        return self.count
    
    def enqueue(self,element):
        if not self.isQueueFull():
            self.front+=1
            self.data[self.front]=element
            self.count+=1
            return self.count
        else:
            return None
        
    def dequeue(self):
        if not self.isQueueEmpty():
            self.count-=1
            return self.data.pop(0)
        else:
            return None
        
    def peek(self):
        if not self.isQueueEmpty():
            return self.data[0]
        else:
            return None
        
    def printElements(self):
        return self.data    