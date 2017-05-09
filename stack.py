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
        else
            return False

    def push(self, value):
        self.elements.insert(0, value) #inserts in front of 0th position

    def pop(self):
        self.elements.pop() #lol


