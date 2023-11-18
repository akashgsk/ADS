from simplestack import Stack

def testEmptyStack():
    s1 = Stack()
    assert s1.getCount() == 0
    assert s1.isStackEmpty() == True

def testPush():
    s2 = Stack()
    s2.push(100)
    assert s2.getCount() == 1
    assert s2.peek() == 100

def testPop():
    s3 = Stack()
    s3.push(200)
    s3.push(300)
    s3.push(400)
    assert s3.getCount() == 3
    assert s3.peek() == 400
    assert s3.pop() == 400
    assert s3.getCount() == 2
    assert s3.printElements() == [200, 300]

testEmptyStack()
testPush()
testPop()
