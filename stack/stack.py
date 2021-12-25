class Stack():
    def __init__(self):
        # initialize stack with empty list values
        myStack = []

    def push(self, value):
        # push value to the top of the stack
        myStack.append(value)
    
    def pop(self):
        # remove top element of the stack and return it
        # if stack is empty, return "Stack is empty"
        if len(myStack) == 0:
            return "Stack is empty"
        else:
            return myStack.pop()

    def top(self):
        # return element at the top of the stack
        # if stack is empty, return "Stack is empty"
        if len(myStack) == 0:
            return "Stack is empty"
        else:
            return myStack[0]

    def get_size(self):
        # return size of stack
        return len(myStack)
    
    def clear(self):
        # remove all elements from the stack
        myStack.clear()
