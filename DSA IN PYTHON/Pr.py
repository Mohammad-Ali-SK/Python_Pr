# # Singly Linked List----------------

# class Node:
#     def __init__(self,data = None, next = None):
#         self.data = data
#         self.next = next
        
# class SLL:
#     def __init__(self):
#         self.head = None
        
        
#     def insert_at_beg(self,data):
#         node = Node(data,self.head)
#         self.head = node
        
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
    
#     def remove_at(self,index):
#         if index < 0 or index > self.get_length():
#             raise Exception('invalid index...')
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
            
            
#     def insert_at(self,data,index):
#         if index < 0 or index > self.get_length():
#             raise  Exception('invalid index...')
#         if index == 0:
#             self.insert_at_beg(data)
#             return
#         itr = self.head
#         count = 0
#         while itr:
#             if count == index-1:
#                 node = Node(data,itr.next)
#                 itr.next = node
#                 break
#             itr = itr.next
#             count += 1
            
#     def insert_after_val(self,data,ins_val):
#         if self.head is None:
#             return
#         if self.head.data == data:
#             self.head.next = Node(ins_val,self.head.next)
#             return
#         itr = self.head
#         while itr:
#             if itr.data == data:
#                 itr.next = Node(ins_val,itr.next)
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
            
            
    
            
#     def print(self):
#         if self.head is None:
#             print('list is empty.....')
#             return
#         itr = self.head
#         listr = ''
#         while itr:
#             listr += str(itr.data) + '-->'
#             itr = itr.next
#         print(listr)
        
# if __name__ == '__main__':
#     li = SLL()
#     li.insert_at_beg(89)
#     li.insert_at_beg(88)
#     li.insert_at_end(90)
#     li.insert_at_end(91)
#     li.print()
#     # li.remove_at(1)
#     # li.remove_at(0)
#     # li.insert_at(78,1)
#     li.insert_after_val(88,900)
#     li.remove_val(88)
#     li.print()
