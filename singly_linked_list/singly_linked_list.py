class Node:
    def __init__(self, value = None, next_node = None):
        self.value = value
        self.next_node = next_node
        
    def __str__(self):
        return f'{self.value}'

class LinkedList:
    def __init__(self):
        self.size = 0
        self.first_node = None
        self.last_node = None

    def __len__(self):
        return len(self.size)

    def new_tail(self, value):
        new_node = Node(value, None)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_tail(self):
        if not self.head:
            return None
        
        if self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        
        current = self.head

        while current.get_next() is not self.tail:
            current = current.get_next()

        value = self.tail.get_value()
        self.tail = current
        return value
            
    def remove_head (self):
        if not self.head:
            return None

        if not self.head.get_next():
            head = self.head
            self.head = None
            self.tail = None

            return head.get_value()

        value = self.head.get_value()
        self.head = self.head.get_next()
        
        return value
            
    def get_length(self):
        if self.head == None:
            return None
        
        length = self.head.get_value()
        current = self.head.get_next()
        
        while current:
            if current.get_value() > length:
                length = current.get_value()