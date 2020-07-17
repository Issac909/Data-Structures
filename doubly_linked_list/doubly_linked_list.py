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
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        self.length -= 1
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
           
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
        head = self.head      
        self.length += 1
        
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node        
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):            
        value = self.head.value
        self.delete(self.head)
        return value

            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
            
        else:
            node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        remove = self.tail.value 
        self.delete(self.tail)
        return remove
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node == self.head:
            pass
            
        elif node == self.tail:
            self.remove_from_tail()
        
        else:
            node.delete()
            self.length -= 1
            
        self.add_to_head(node.value)
    
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node == self.tail:
            pass

        elif node == self.tail:
            self.remove_from_head()
            self.add_to_tail(node.value)
                
        else:
            node.delete()
            self.add_to_tail(node.value)
        

        
            
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