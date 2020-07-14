"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
- Using an array limits the amount of elements but you still have access to the index. Using a Queue refers to FIFO (First in First out) and allows for unlimited elements, adding elements only to the end of the linked list. So you can imagine pulling napkins from a napkin holder that seemingly never ends.
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# 1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class ArrQueue:
    def __init__(self):
        self.size = 0
        self.storage = []
        
    def __len__(self):
        return self.size
    
    def enqueue(self, value):
        self.size += 1
        self.storage.append(value)
    
    def dequeue(self):
        if self.size == 0:
            return None
        
        else:
            self.size -= 1
            return self.storage.pop(0)
        
# 2 
class LLQueue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
        # self.storage = ?
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        if self.last is None:
            self.head = Node(value)
            self.last = self.head
        else:
            self.last.next = Node(value)
            self.last = self.last.next

    def dequeue(self):
        if self.head is None:
            return None
        else: 
            self.size -= 1
            new_head = self.head.value
            self.head = self.head.next
            return new_head

array_queue = ArrQueue()
LLQueue = LLQueue()