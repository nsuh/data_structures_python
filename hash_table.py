import numpy as np
from bitarray import bitarray

class Stack:
    def __init__(self):
        self.elements = np.empty(10)
        self.elements[:] = np.NAN
        
        self.prime_key = 7
    
    def hash(self, value):
        
        hash_value = 0
        #if value is a string, sum up ascii values of each letter
        if isinstance(value, basestring): 
            for letter in value:
                hash_value += ord(letter)
        elif isinstance(value, (int, long)):
            hash_value = value
            
            
        hash_value = 
    
    def resize(self):
        
        #make new stack, with doubled size
        new_elements = np.empty(2*size(self.elements))
        new_elements[:] = np.NAN
        
        #choose new prime for hash fn
        self.prime_key = self.find_next_prime(self.prime_key + 1)
        
        #rehash
        for elem in self.elements:
            hash(elem)
            
            
        
      
    
    
    #finds next prime.  Took code from https://gist.github.com/ldong/808d5403c5e3b19f2f05
    def find_next_prime(n):
        return self.find_prime_in_range(n, 2*n)

    def find_prime_in_range(a, b):
        for p in range(a, b):
            for i in range(2, p):
                if p % i == 0:
                    break
            else:
                return p
        return None