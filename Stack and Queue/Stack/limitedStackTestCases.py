from limitedStack import stack

def testEmptyStack():
    s1 = stack()
    assert s1.getCount() == 0
    assert s1.isStackEmpty() == True
    assert s1.isStackFull() == False

def testPush():
    s2 = stack()
    s2.push(100)
    assert s2.getCount() == 1
    assert s2.peek() == 100

def testPop():
    s3 = stack()
    s3.push(200)
    s3.push(300)
    s3.push(400)
    s3.push(500)
    assert s3.isStackFull() == False
    s3.push(600)
    assert s3.isStackFull() == True
    assert s3.getCount() == 5
    assert s3.peek() == 600
    assert s3.pop() == 600
    assert s3.getCount() == 4
    assert s3.printElements() == [200, 300, 400, 500]

testEmptyStack()
testPush()
testPop()