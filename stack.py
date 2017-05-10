#stack.py
#this is a stack implementation in python.

#misc notes:
#methods - for classes.  functions - general
#the first argument in a method definition header is a reference to 
#   the object (self)

class Stack:
    def __init__(self):
        self.elements = [] #python list
    
    def isEmpty(self):
        if len(self.elements) == 0:
            return True
        else:
            return False

    def push(self, value):
        self.elements.insert(0, value) #inserts in front of 0th position

    def pop(self):
        return self.elements.pop(0) 

    def top(self):
        return self.elements[0]

if __name__ == "__main__":
    myStack = Stack()
    myStack.push(10)
    myStack.push(20)
    myStack.push(30)
    print myStack.top()
    myStack.pop()
    print myStack.top()
    myStack.pop()
    print myStack.top()
    myStack.pop()
