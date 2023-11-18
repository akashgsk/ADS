from simpleQueue import SimpleQueue

def testEmptyQueue():
    q1 = SimpleQueue()
    assert q1.getElementCount() == 0
    assert q1.isQueueEmpty() == True

def testEnqueue():
    q2 = SimpleQueue()
    q2.enqueue(45)
    assert q2.getElementCount() == 1
    assert q2.peek() == 45

def testDequeue():
    q3 = SimpleQueue()
    q3.enqueue(67)
    q3.enqueue(7)
    q3.enqueue(12)
    assert q3.getElementCount() == 3
    assert q3.peek() == 67
    assert q3.dequeue() == 67
    assert q3.getElementCount() == 2
    assert q3.printElements() == [7, 12]

testEmptyQueue()
testEnqueue()
testDequeue()