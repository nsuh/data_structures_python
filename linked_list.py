#linked list implementation

class ll_node:
    def __init__(self, init_data=None):
        self.next = None
        self.data = init_data

class linked_list:
    def __init__(self):
        self.head = None
        
    def insert_front(self, value):
        new_node = ll_node(value)
        new_node.next = self.head
        self.head = new_node
        
    def delete_node(self, value):
        prev_node = None
        current_node = self.head
        while current_node.data != value:
            prev_node = current_node
            current_node = current_node.next
        if prev_node is not None:
            prev_node.next = current_node.next  #linked list "jumps" over current node
        elif prev_node is None:
            self.head = self.head.next
        
        
    def print_ll(self):
        current_node = self.head
        while current_node.next is not None:
            print current_node.data
            current_node = current_node.next
        print current_node.data  #print tail node

if __name__ == "__main__":
    #test insertion
    a = linked_list()
    a.insert_front(1)
    a.insert_front(2)
    a.insert_front(3)
    a.insert_front(4)
    a.print_ll()
    print "\n"

    #test deletion
    print "delete 2"
    a.delete_node(2)
    a.print_ll()
    print "\n"

    print "insert 5, 6"
    a.insert_front(5)
    a.insert_front(6)
    a.print_ll()
    print "\n"

    print "delete 1 (tail)"
    a.delete_node(1)
    a.print_ll()
    print "\n"

    print "delete 6 (head)"
    a.delete_node(6)
    a.print_ll()
    print "\n"