class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next
        
class SLL:
    def __init__(self):
        self.head = None
    def insert_fs(self,data):
        node = Node(data,self.head)
        self.head = node
    
    def insert_last(self,data):
        if self.head is None:
            node = Node(data,None)
            self.head = node
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def insert_at(self,index,data):
        if index < 0 or index > self.get_length():
            raise Exception('invalid index')
        if index == 0:
            self.insert_fs(data)
            return
        itr = self.head
        count = 0
        while itr:
            if count == index -1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1
        
            
    def insert_after(self,data,ins_data):
        if self.head is None:
            return None
        if self.head.data == data:
            self.head.next =  Node(ins_data,self.head.next)
            return
        itr = self.head
        while itr:
            if itr.data == data:
                itr.next = Node(ins_data,itr.next)
                break
            itr = itr.next
    
    def delete_at(self,index):
        if index < 0 or index > self.get_length():
            raise Exception('invalid index...')
        if index == 0:
            self.head = self.head.next
            return 
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
    
    def delete_val(self,data):
        if  self.head is None:
            return None
        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head
        while itr:
            if itr.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next
            
                
    def print_all(self):
        if self.head is None:
            print('There is no element are here...')
            return
        itr = self.head
        listr = ' '
        while itr:
            listr += str(itr.data)  + '-->'
            itr = itr.next
        print(listr)
    
# if __name__ == '__main__':
#     li = SLL()
#     li.insert_fs(9)
#     li.insert_fs(8)
#     li.insert_fs(7)
#     li.insert_last(10)
#     li.insert_last(11)
#     li.print_all()
#     # li.delete_at(0)
#     # li.insert_after(9,12)
#     # li.delete_val(10)
#     # li.insert_at(0,5)
#     li.print_all()


 