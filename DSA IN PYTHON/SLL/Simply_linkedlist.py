# class Node:
#     def __init__(self,data=None,next = None):
#         self.data = data
#         self.next = next


# class SLL:
#     def __init__(self):
#         self.head = None
    
#     def insert_at_start(self,data):
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
        
#     def insert_list(self,list_data):
#         for i in list_data:
#             self.insert_at_end(i)
            
#     def get_length(self):
#         itr = self.head
#         count = 0
#         while itr:
#             count += 1
#             itr = itr.next
#         return count
    
#     def insert_at(self,index,ins_d):
#         if index < 0 or index > self.get_length():
#             raise Exception('Invalid index.')
#         if index == 0:
#             self.insert_at_start(ins_d)
#             return
#         itr = self.head
#         count = 0
#         while itr:
#             if count == index -1:
#                 node = Node(ins_d,itr.next)
#                 itr.next = node
#                 break
#             itr = itr.next
#             count += 1
            
#     def remove_at(self,index):
#         if index < 0 or index > self.get_length():
#             raise Exception('Invalid index.')
#         if index == 0:
#             self.head = self.head.next
#             return
#         itr = self.head
#         count = 0
#         while itr:
#             if count == index-1:
#                 itr.next = itr.next.next
#                 break
#             itr = itr.next
#             count += 1
        
#     def insert_a_val(self,data,ins_d):
#         if self.head is None:
#             return
#         if self.head.data == data:
#             self.head.next = Node(ins_d,self.head.next)
#             return
#         itr = self.head
#         while itr:
#             if itr.data == data:
#                 itr.next = Node(ins_d,itr.next)
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
#             if itr.data == data:
#                 itr.next = itr.next.next
#                 itr = itr.next
            
            
        
        
        
        
#     def print(self):
#         if self.head is None:
#             print('Linked list is empty...')
#             return
#         itr = self.head
#         listr = ''
#         while itr:
#             listr += str(itr.data) + '-->'
#             itr = itr.next
#         print(listr)
        
        
# if __name__ == '__main__':
#     li = SLL()
#     # li.insert_at_end(90)
#     # li.insert_at_end(91)
#     # li.insert_at_start(89)
#     # li.insert_at_start(88)
#     li.insert_list(['Amir','Sumi','Rimi','Rup', 'Sumon','Rohit'])
#     li.print()
#     # li.insert_at(3,'Roj')
#     # li.remove_at(5)
#     # li.insert_a_val('Amir','jamn')
#     li.remove_val('Amir')
#     li.print()
