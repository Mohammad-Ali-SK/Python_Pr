class Node:
    def __init__(self,data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next
class CDLL:
    def __init__(self,head = None):
        self.head = None
    
    def insert_f(self,data):
        node = Node(data)
        if self.head is None:
            node.next = node
            node.prev = node
        else:
            node.next = self.head
            node.prev = self.head.prev
            self.head.prev.next = node
            self.head.prev = node
        self.head = node
        
    def insert_last(self,data):
        node = Node(data)
        if self.head is None:
            node.next = node
            node.prev = node
            self.head = node
        else:
            node.next = self.head
            node.prev = self.head.prev
            self.head.prev.next = node
            self.head.prev = node
            
            
    
            
            
    def insert_after(self,temp,data):
        if temp is not None:
            node = Node(data)
            node.next = temp.next
            node.prev = temp
            temp.next.prev = node
            temp.next = node
            
            
            
            
            
    
    def print_all(self):
        itr = self.head
        if itr is not None:
            print(itr.data,end ='-->')
            itr = itr.next
        while itr != self.head:
            print(itr.data,end = '-->')
            itr = itr.next
    
    
    
    
if __name__ == '__main__':
    li = CDLL()
    li.insert_f(98)
    li.insert_last(8)
    li.insert_last(77)
    li.insert_last(6)
    li.print_all()