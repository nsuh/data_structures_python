#hash table with linear probing.  handles ints and strings.

import numpy as np

class Hash_table:
    def __init__(self):
        self.elements = np.empty(10)
        self.elements[:] = np.NAN
        
        self.prime_key = 7
    
    #handles only strings and ints, for the time being
    def hash(self, value):
        
        if np.isnan(value):
            return
        #if number of elements in table is greater than half of table, resize
        if sum(~np.isnan(self.elements)) > (self.elements.size / 2):
            self.resize()
        
        hash_value = 0
        #if value is a string, sum up ascii values of each letter
        if isinstance(value, basestring): 
            for letter in value:
                hash_value += ord(letter)
        elif isinstance(value, (int, long)):
            hash_value = value
        else:
            print "error: input now a string or int"
            
        hash_value = hash_value % self.prime_key
        
        if np.isnan(self.elements[hash_value]): #empty, put key in hash table
            self.elements[hash_value] = value
            #print "empty"
            return
        elif self.elements[hash_value] == value:  #already in table
            #print "already in table"
            return
        elif self.elements[hash_value] != value:  #collision
            #print "collision"
            i = 0
            #linear probing
            while (not np.isnan(self.elements[hash_value + i])): 
                if self.elements[hash_value + i] == value: #already in table
                    return
                i += 1
            self.elements[hash_value + i] = value
            return
        
    
    def resize(self):
        print "resizing"
        #make new stack, with doubled size
        new_elements = np.empty(2*self.elements.size)
        new_elements[:] = np.NAN
        old_stuff = self.elements
        self.elements = new_elements
        
        #choose new prime for hash fn
        self.prime_key = self.find_next_prime(self.prime_key + 1)
        
        #rehash
        for elem in old_stuff:
            if not np.isnan(elem):
                self.hash(int(elem))
      
    
    
    #finds next prime.  Took code from https://gist.github.com/ldong/808d5403c5e3b19f2f05
    def find_next_prime(self, n):
        return self.find_prime_in_range(n, 2*n)

    def find_prime_in_range(self, a, b):
        for p in range(a, b):
            for i in range(2, p):
                if p % i == 0:
                    break
            else:
                return p
        return None
    
if __name__ == "__main__":
    a = Hash_table()
    a.hash(0)
    a.hash(5)
    a.hash(6)
    a.hash(13)
    a.hash(20)
    a.hash(49)
    print a.elements

    a.hash(50)
    a.hash(51)


    print a.elements