from unlimitedstack import UnlimitedStack
from unlimitedstack import Node

def testEmptyUnlimitedStack():
    s1 = UnlimitedStack()
    assert s1.getCount() == 0
    assert s1.isStackEmpty() == True

def testPushUnlimitedStack():
    s2 = UnlimitedStack()
    s2.push(1000)
    assert s2.getCount() == 1
    assert s2.peek() == 1000

def testPopUnlimitedStack():
    s3 = UnlimitedStack()
    s3.push(2000)
    s3.push(3000)
    s3.push(4000)
    assert s3.getCount() == 3
    assert s3.peek() == 4000
    assert s3.pop() == 4000
    assert s3.getCount() == 2
    assert s3.printElements() == [3000, 2000]

testEmptyUnlimitedStack()
testPushUnlimitedStack()
testPopUnlimitedStack()
