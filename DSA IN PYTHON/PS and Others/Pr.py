class Node:
    def __init__(self,data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next
class CDLL:
    def __init__(self,head = None):
        self.head = None
    
    def insert_fs(self,data):
        node = Node(data)
        if self.head is None:
            node.prev = node
            node.next = node
        else:
            node.next = self.head
            node.prev = self.head.prev
            self.head.prev.next = node
            self.head.prev = node
        self.head = node
    
    def insert_ls(self,data):
        node = Node(data)
        if self.head is None:
            node.next = node
            node.prev = node
            self.head = node
        else:
            node.next =  self.head
            node.prev = self.head.prev
            node.prev.next = node
            self.head.prev = node
        
        
    def search_node(self,data):
        if self.head is None:
            return None
        if self.head.data == data:
            return self.head
        itr = self.head 
        while itr != self.head:
            if itr.data == data:
                return itr
            itr = itr.next
        return None
            
            
    def insert_after(self,temp,data):
        if temp is not None:
            node = Node(data)
            node.next = temp.next
            node.prev = temp
            temp.next.prev = node
            temp.next = node
    
    def print_all(self):
        if self.head is None:
            return None
        itr = self.head
        if itr is not None:
            print(itr.data,end ='-->')
            itr = itr.next
        while itr != self.head:
            print(itr.data,end = '-->')
            itr = itr.next
            
            
            
    def delete_frist(self):
        if self.head is not None:
            if self.head.next == self.head:
                self.head = None
            else:
                self.head.prev.next = self.head.next
                self.head.next.prev = self.head.prev
                self.head = self.head.next
    def delete_last(self):
        if self.head is not None:
            if self.head.next == self.head:
                self.head = None
                return
            else:
                self.head.prev.prev.next = self.head
                self.head.prev = self.head.prev.prev
                
    def delete_item(self,data):
        if self.head is None:
            return None
        if self.head.next == self.head:
            if self.head.data == data:
                self.head = None
                return
        else:
            itr = self.head
            if self.head.data == data:
                self.delete_frist()
            else:
                itr = itr.next
                while itr is not self.head:
                    if itr.data == data:
                        itr.prev.next = itr.next
                        itr.next.prev = itr.prev
       
        
li = CDLL()
li.insert_fs(8)
li.insert_fs(7)
li.insert_fs(6)
li.insert_ls(9)
li.insert_ls(10)
li.print_all()