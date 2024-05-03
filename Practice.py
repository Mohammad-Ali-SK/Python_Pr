class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next
class CLL:
    def __init__(self,last = None):
        self.last = None
    
    def insert_frist(self,data):
        node = Node(data)
        if self.last is None:
            node.next = node
            self.last = node
        else:
            node.next = self.last.next
            self.last.next = node
    
    def insert_last(self,data):
        node = Node(data)
        if self.last is None:
            node.next = node
            self.last = node
        else:
            node.next = self.last.next
            self.last.next = node
            self.last = node
    
    def print_all(self):
        if self.last is None:
            return None
        itr = self.last.next
        while itr != self.last:
            print(itr.data,end = '--')
            itr = itr.next
        print(itr.data)
    
    
    def search(self):
        if self.last is None:
            return None
        if self.last.data == data:
            return self.last.data
        itr = self.last.next
        while itr != self.last:
            if itr.data == data:
                return itr
            itr = itr.next
    
    def insert_after(self,temp,data):
        if temp is not None:
            node = Node(data,temp.next)
            temp.next = node
            if temp == self.last:
                self.last = node
    
    
    