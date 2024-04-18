class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next
class CLL:
    def __init__(self,last = None):
        self.last = last
        
    
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
            node.next  = self.last.next
            self.last.next = node
            self.last = node

    def print_all(self):
        if self.last is None:
            return
        itr = self.last.next
        while itr != self.last:
            print(itr.data,end ='-->')
            itr = itr.next
        print(itr.data)
    

    def search_node(self,data):
        if self.last is None:
            return None
        if self.last.data == data:
            return self.last.data
        itr = self.last.next
        while itr!=self.last:
            if itr.data == data:
                return itr
            itr = itr.next
    
    
    def insert_after(self,temp,data):
        if temp is not None:
            node  = Node(data,temp.next)
            temp.next = node
            if temp == self.last:
                self.last = node
    
  
    def delete_frist(self):
        if self.last is not None:
            if self.last.next == self.last:
                self.last = None
            else:
                self.last.next = self.last.next.next 
    
    
    def delete_last(self):
        if self.last is not None:
            if self.last.next == self.last:
                self.last = None
            else:
                itr = self.last.next
                while itr.next != self.last:
                    itr = itr.next
                itr.next = self.last.next
                self.last = itr
            
                
                
                
                
                
                
                
    def delete_item(self,data):
        if self.last is not None:
            if self.last.next == self.last:
                if self.last.data == data:
                    self.last = None
            else:
                if self.last.next == self.last:
                    self.delete_frist()
                else:
                    itr = self.last.next
                    while itr != self.last:
                        if itr.next == self.last:
                            if self.last.data == data:
                                self.delete_last()
                                break
                        if itr.next.data == data:
                            itr.next = itr.next.next
                            break
                        itr = itr.next
                
        
if __name__ == '__main__':
    li = CLL()
    li.insert_frist(88)
    li.insert_frist(87)
    li.insert_last(90)
    li.insert_last(91)
    li.insert_after(li.search_node(90),900)
    li.print_all()
    # li.delete_frist()
    # li.delete_last()
    li.delete_item(90)
    li.print_all()
     