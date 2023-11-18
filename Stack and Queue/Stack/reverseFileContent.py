from simplestack import Stack

def reverse(file):
    s1 = Stack()
    
    with open(file, 'r') as input_file:
        lines = input_file.readlines()

    for line in lines:
        s1.push(line.strip())  # to remove newline characters

    with open(file, 'w') as output_file:
        while not s1.isStackEmpty():
            reversed_line = s1.pop()
            output_file.write(reversed_line + '\n')  # Add newline character to write lines to the file
            print(reversed_line)  

reverse('sample.txt')
