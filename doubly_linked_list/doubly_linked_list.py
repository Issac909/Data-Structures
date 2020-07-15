"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
        

           
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node
        self.head.prev = ListNode(None)
        self.length += 1
        
        if self.head == None or self.tail is None:
            self.head.next = self.tail
            self.tail.prev = self.head
            
        else:
            new_node.prev = ListNode(None)
            new_node.next = ListNode(None)
            self.head = new_node
            self.tail= new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None and self.tail is None:
            return None
        
        else:
            value = self.head.value
            self.head = None
            self.tail = None 
            self.length -= 1
            return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        new_node.prev = self.tail
        self.tail = new_node
        self.tail.next = None
        self.length += 1
        
        if self.__len__() == 2:
            self.head.next = self.tail
            self.tail.prev = self.head
            
        elif self.head is None or self.tail is None:
            new_node.prev = ListNode(None)
            new_node.next = ListNode(None)
            self.head = new_node
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        self.length -= 1
        prev_tail = self.tail
        
        if prev_tail.prev:
            self.tail = prev_tail.prev
            new_tail = prev_tail.prev
            new_tail.value = None
            
        else:
            self.tail = None
            self.head = None
        
        self.length -= 1
        return prev_tail.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        current_head = self.head
        
        while current_head is not node:
            current = current.next
        
        if current_head.prev:
            prev = current.prev
            prev.next = current.next
            
        if current.next:
            after = current.next
            after.prev = current.prev
            
        prev_head = self.head
        prev_head.prev = current
        current.next = prev_head
        current.prev = None
        self.head = current
  
  
  
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        current = self.head
        
        while current is not node:
            current = current.next
        
        if current.prev:
            prev = current.prev
            prev.next = current.next
            if node == self.tail:
                self.tail = prev
                
        if current.next:
            new_next = current.next
            new_next.prev = current.prev
            if node is self.head:
                self.head = new_next
                
        prev_tail = self.tail
        prev_tail.next = current
        current.prev = prev_tail
        current.next = None
        self.tail = current
        
    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        self.length -= 1
        current = self.head
        while current != node:
            current = current.next
        if node == self.head and node == self.tail:
            self.head = None
            self.tail = None
        if current.prev:
            before = current.prev
            before.next = current.next
            if node == self.tail:
                self.tail = before
        if current.next:
            after = current.next
            after.prev = current.prev
            if node == self.head:
                self.head = after
        
            
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        current = self.head 
        highest_value = 0
        
        while current:
            if current.value > highest_value:
                highest_value = current.value
            
            current = current.next
            
        return highest_value