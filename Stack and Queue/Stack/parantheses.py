from simplestack import Stack
input="([{"
output=")]}"


s1=Stack()
def checkForParantheses(input_string):
    f=0
    for i in input_string:
        #If char is in the "input" string then that will be pushed to stack
        if i in input:
            s1.push(i)
        elif i in output:
            #If char is in "output" then the last element from stack is popped and compared with index of input
            if not s1.isStackEmpty():
                if(input.index(s1.pop())==output.index(i)):
                   f=0
                else:
                    f=1
                    break
            else:
                f=1
                break
    if(f==1):
        return False
    else:
        return True

def fileCheck(filename):
    with open(filename,'r')as f:
        for line in f:
            assert(checkForParantheses(line)==True)

			
assert(checkForParantheses("(({[[{{}}]]}))")==True)       
assert(checkForParantheses("(({{}]]}))")==False)
fileCheck("parantheses.txt")