"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
   
- You can only add a predetermined amount of elements inside an array using index. Where as with a linked list, you can add as many as you want, and with specifically stacks, to the head of the list or LIFO. You can imagine adding and removing pancakes from an unlimited stack of pancakes.
"""

# 1
class ArrStack:
    def __init__(self):
        self.size = 0
        # self.storage = ?
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        return self.storage.insert(0, value)

    def popper(self):
        if len(self.storage) > 0:
            return self.storage.pop(0)
        else: 
            return None

# 2
class Node:
    def __init__(self, value = None, next_node = None):
        self.value = value
        self.next_node = next_node
        
class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = ?
        self.first_node = None
        self.last_node = None

    def __len__(self):
        return len(self.size)

    def push(self, value):
        self.size += 1
        new_node = Node(value)
        
        if self.first_node == None:
            self.first_node = new_node
            self.last_node = new_node
            
        self.last_node.next_node = new_node
        self.last_node = new_node

    def popper(self):
        if self.size > 0:
            node_to_pop = self.last_node
            current_node = self.first_node
        
        elif node_to_pop != current_node:
            while current_node.next_node != node_to_pop:
                current_node = current_node.next_node
                
        elif self.size == 0:
            self.first_node = None
            

arr_stack = ArrStack()
LLStack = Stack()
            
