class Node:
    def __init__(self,prev = None, data = None, next = None):
        self.prev = prev
        self.data = data
        self.next = next
class DLL:
    def __init__(self):
        self.head = None
    
    def insert_at_start(self,data):
        if self.head is None:
            node = Node(None,data,self.head)
            self.head = node
        else:
            node = Node(None,data,self.head)
            self.head.prev = node
            self.head = node
    
    def insert_at_end(self,data):
        if self.head is None:
            node = Node(None,data,None)
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(itr,data,None)
        
        
    def delete_frist(self):
        if self.head is not None:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
    
    
    def delete_last(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head = None
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.prev.next = None
            
            
    def delete_item(self,data):
        if self.head is None:
            return
        else:
            itr = self.head
            while itr is not None:
                if itr.data == data:
                    if itr.next is not None:
                        itr.next.prev = itr.prev
                    if itr.prev is not None:
                        itr.prev.next = itr.next
                    else:
                        self.head = None
                        break
                itr = itr.next
        
        
        
        
    def print_forward(self):
        if self.head is None:
            print('DLL is empty...')
            return
        itr = self.head
        listr = ''
        while itr:
            listr += str(itr.data) + '-->'
            itr = itr.next
        print(listr)
    
    def get_last(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr
    
    def print_backward(self):
         if self.head is None:
             return
         last_node = self.get_last()
         itr = last_node
         listr = ''
         while itr:
             listr += str(itr.data) + '-->'
             itr = itr.prev
             
         print(listr)
             


if __name__ == '__main__':
    li = DLL()
    li.insert_at_end(56)
    li.insert_at_start(89)
    li.insert_at_start(88)
    li.insert_at_end(91)
    li.insert_at_end(92)
    li.insert_at_start(78)
    li.insert_at_end(99)
    li.print_forward()
    # li.delete_frist()
    # li.delete_last()
    li.delete_item(99)
    li.print_forward()
    
    # li.print_backward()
