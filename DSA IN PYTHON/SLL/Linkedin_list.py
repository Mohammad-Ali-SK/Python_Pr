# class Node:
#     def __init__(self,data = None, next = None):
#         self.data = data
#         self.next = next
# class Linkedlist:
#     def __init__(self):
#         self.head = None
#     def insert_at_beg(self,data):
#         node = Node(data,self.head)
#         self.head = node
#     def print(self):
#         if self.head is None:
#             print('linked list is empty.')
#             return
#         itr = self.head
#         listr = ''
#         while itr:
#             listr += str(itr.data) + '-->'
#             itr = itr.next
#         print(listr)
        
#     def insert_at_end(self,data):
#         if self.head is None:
#             self.head = Node(data,None)
#             return
#         itr = self.head
#         while itr.next:
#             itr = itr.next
#         itr.next = Node(data,None)
    
#     def get_length(self):
#         count = 0
#         itr = self.head
#         while itr:
#             count += 1
#             itr = itr.next
#         return count
    
#     def insert_at(self,index,data):
#         if index < 0 or index > self.get_length():
#             raise Exception('invalid index.')
#         if index == 0:
#             self.insert_at_beg(data)
#             return
#         itr = self.head
#         count = 0
#         while itr:
#             if count == index -1:
#                 node = Node(data,itr.next)
#                 itr.next = node
#                 break
#             itr = itr.next
#             count += 1
            
#     def remove_at(self,index):
#         if index < 0 or index > self.get_length():
#             raise Exception('i v i')
#         if index == 0:
#             self.head = self.head.next
#             return
#         itr = self.head
#         count = 0
#         while itr:
#             if count == index - 1:
#                 itr.next = itr.next.next
#                 break
#             itr = itr.next
#             count += 1
            
#     def insert_af_val(self,data,in_val):
#         if self.head is None:
#             return
#         if self.head.data == data:
#             self.head.next = Node(in_val,self.head.next)
#             return
#         itr = self.head
#         while itr:
#             if itr.data == data:
#                 itr.next = Node(in_val,itr.next)
#                 break
#             itr = itr.next
            
#     def remove_val(self,data):
#         if self.head is None:
#             return
#         if self.head.data == data:
#             self.head = self.head.next
#             return
#         itr = self.head
#         while itr.next:
#             if itr.next.data == data:
#                 itr.next = itr.next.next
#                 break
#             itr = itr.next
        
        
            
    

# if __name__ == '__main__':
#     li = Linkedlist()
#     li.insert_at_beg(89)
#     li.insert_at_beg(8)
#     li.insert_at_end(11)
#     li.insert_at_end(100)
#     print(li.get_length())
#     li.print()
#     # li.insert_at(1,888)
#     # li.remove_at(3)
#     li.insert_af_val(8,78)
#     li.insert_af_val(100,200)
#     li.remove_val(200)
#     li.remove_val(8)
#     li.print()


class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class SLL:
    def __init__(self):
        self.head = None
    
    def insert_frist(self,data):
        node = Node(data,self.head)
        self.head = node
    
    def insert_last(self,data):
        if self.head is None:
            node = Node(data,None)
            self.head = node
            return
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
            raise Exception('Invalid index')
        if index == 0:
            self.insert_frist(data)
            return
        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1
        
    def delete_at(self,index):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid inde')
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
            
    def insert_af_val(self,data,in_d):
        if self.head is None:
            return None
        if self.head.data == data:
            self.head.next = Node(in_d,self.head.next)
            return
        itr = self.head
        while itr:
            if itr.data == data:
                itr.next = Node(in_d,itr.next)
                break
            itr = itr.next
    
    def delete_val(self,data):
        if self.head is None:
            return None
        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head
        while itr.next:
            if itr.data == data:
                itr.next = itr.next.next
            itr = itr.next
            
            
    def print_all(self):
        if self.head is None:
            return None
        itr = self.head
        listr = ''
        while itr:
            listr += str(itr.data) + '-->'
            itr = itr.next
        print(listr)
        
if __name__ == '__main__':
    s = SLL()
    s.insert_frist(9)
    s.insert_frist(8)
    s.insert_frist(7)
    s.insert_last(10)
    s.insert_last(11)
    s.insert_last(12)
    s.insert_af_val(9,77)
    s.delete_at(1)
    s.print_all()