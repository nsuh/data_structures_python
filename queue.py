#stack.py
#this is a queue implementation in python.


class Queue:
    def __init__(self):
        self.elements = [] #python list
    
    def isEmpty(self):
        if len(self.elements) == 0:
            return True
        else:
            return False

    def enqueue(self, value):
        self.elements.insert(len(self.elements), value) 

    def dequeue(self):
        return self.elements.pop(0) 

    def top(self):
        return self.elements[0]

if __name__ == "__main__":
    myStack = Queue()
    myStack.enqueue(10)
    myStack.enqueue(20)
    myStack.enqueue(30)
    print myStack.top()
    myStack.dequeue()
    print myStack.top()
    myStack.dequeue()
    print myStack.top()
    myStack.dequeue()

