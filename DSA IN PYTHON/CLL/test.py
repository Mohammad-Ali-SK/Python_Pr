class Node:
    def __init__(self,data = None,prev = None,next = None):
        self.data = data
        self.prev = prev
        self.next = next

class CDL:
    def __init__(self,head = None):
        self.head = head
    
    
    def insert_f(self,data):
        node = Node(data)
        if self.head is None:
            node.next = node
            node.prev = node
            self.head = node
        else:
            node.next = self.head
            node.prev = self.head.prev
            self.head.prev.next = node
            self.head.prev= node
            self.head = node
    
    def insert_last(self,data):
        node = Node(data)
        if self.head is None:
            node.next = node
            node.prev  = node
            self.head = node
        else:
            node.next = self.head
            node.prev = self.head.prev
            node.prev.next = node
            self.head.prev = node
    
    def search_node(self,data):
        if self.head is not None:
            if self.head.next == self.head:
                if self.head.data == data:
                    return self.head
            else:
                