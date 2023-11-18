from limitedQueue import LimitedQueue

def testEmptyQueue():
    q1 = LimitedQueue()
    assert q1.getCount() == 0
    assert q1.isQueueEmpty() == True
    assert q1.isQueueFull() == False

def testEnqueue():
    q2 = LimitedQueue()
    q2.enqueue(15)
    assert q2.getCount() == 1
    assert q2.peek() == 15

def testDequeue():
    q3 = LimitedQueue()
    q3.enqueue(25)
    q3.enqueue(35)
    q3.enqueue(45)
    q3.enqueue(55)
    q3.enqueue(65)
    assert q3.isQueueFull() == True
    assert q3.getCount() == 5
    assert q3.peek() == 25
    assert q3.dequeue() == 25
    assert q3.getCount() == 4
    assert q3.printElements() == [35, 45, 55, 65]

testEmptyQueue()
testEnqueue()
testDequeue()