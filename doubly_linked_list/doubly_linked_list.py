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
        new_node = ListNode(value, None)

        if not self.head:
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
        if not self.head:
            return None

        if not self.head.next:

            head = self.head.next
            self.head = None
            self.tail = None
            return head.value
        
        value = self.head.value

        self.head = self.head.next
        self.head.prev = None
        return value

            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value, None)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
            
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if not self.head:
            return None
        
        if self.head is self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
            return value
        current = self.head

        while current.next is not self.tail:
            current = current.next

        value = self.tail.value
        self.tail = current
        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        current = self.head

        while current:
            if current == node:
                old_head = self.head
                current.prev = None
                current.next = old_head
                self.head = current
            current = current.next
        return None
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        current = self.head

        while current:
            if current == node:
                old_tail = self.tail
                current.next = None
                current.prev = old_tail
                self.tail = current
            current = current.next
        return None

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        current = self.head

        while current:
            if current is not node:
                current = current.next
            if current is node:
                current.prev = current.next.prev
    
                


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None
        
        max_value = self.head.value

        current = self.head.next.value

        while current:
            if current > max_value:
                max_value = current
            
            current = current.next.value

        return max_value