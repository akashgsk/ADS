from simplestack import Stack

S = Stack()
T = Stack()

def transfer(S, T):
    # Creating a temporary stack for storing the data from stack S while copying to it to stack T
    temp = Stack()
    while S.getCount() > 0:
        temp.push(S.pop())
    while temp.getCount() > 0:
        T.push(temp.pop())
    return T.printElements()

# Example usage
S.push(11)
S.push(23)
S.push(35)
S.push(49)

print("Contents of Stack S before transfer :\n", S.printElements())
result = transfer(S, T)
print("Contents copied to Stack T :\n",result)