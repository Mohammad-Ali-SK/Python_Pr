# class Stack:
#     def __init__(self):
#         self.stack = []
#     def is_empty(self):
#         return len(self.stack) == 0
#     def push_data(self,data):
#         self.stack.append(data)
#     def pop_data(self,data):
#         if not self.is_empty():
#             return self.stack.pop(data)
#         raise IndexError('stack is empty...')
#     def check_size(self):
#         if not self.is_empty():
#             return len(self.stack)
#         raise IndexError('There is no item in the stack')
    
#     def peek_data(self):
#         if not self.is_empty():
#             return self.stack[-1]
#         raise IndexError('there is not element..')
    
    
    
    
# if __name__ == '__main__':
#     li = Stack()
#     li.push_data(8)
#     li.push_data(7)
#     li.push_data(6)
#     print(li.stack)
#     print(li.peek_data())


# Day -2------------------------------------------------------------------ Stack day 2

# from typing import SupportsIndex


# class Stack(list):
#     def is_empty(self):
#         return len(self) == 0
#     def push_data(self,data):
#         self.append(data)
#     def pop(self):
#         if not self.is_empty():
#             return super().pop()
#         raise IndexError('Stack is Empty..')
#     def peek(self):/
#         if not self.is_empty():
#             return self[-1]
#         raise IndexError('Stack is empty...')
#     def size(self):
#         return len(self)
#     def insert(self,index,data):
#         raise AttributeError('No attribute in stack...')

# s1 = Stack()
# s1.push_data(8)
# s1.push_data(7)
# s1.insert(0,8)
# print(s1)

# Day --------------------------------------------------------------- Day-3 --Stack

# class Node:
#     def __init__(self,data = None, next = None):
#         self.data = data
#         self.next = next
# class Stack:
#     def __init__(self):
#         self.head = None
#         self.count = 0
        
#     def is_empty(self):
#         return self.head == None
    
#     def push_data(self,data):
#         node = Node(data,self.head)
#         self.head = node
#         self.count += 1
    
#     def pop_data(self):
#         if not self.is_empty():
#             data = self.head.data
#             self.head = self.head.next
#             self.count -= 1
#             return data
#         else:
#             raise IndexError("Stack is empty..")
        
#     def peek(self):
#         if not self.is_empty():
#             return self.head.data
#         else:
#             raise IndexError('Stack is empty.')
#     def size(self):
#         return self.count
    
#     def stack_data(self):
#         if self.head is None:
#             raise Exception('There are no element in the stack..')
#         itr = self.head
#         listr = []
#         while itr:
#             listr.append(itr.data)
#             itr = itr.next
#         print(listr)
# Day- 4.)--------------------------------------------------------------------------------Day--4. Stack in python

# class Node:
#     def __init__(self,data = None, next = None):
#         self.data = data
#         self.next = next
# class SLL:
#     def __init__(self):
#         self.head = None
    
#     def insert_frist(self,data):
#         node = Node(data,self.head)
#         self.head = node
    
#     def insert_last(self,data):
#         if self.head is None:
#             self.head = Node(data,None)
#             return
#         itr = self.head
#         while itr.next:
#             itr = itr.next
#         itr.next = Node(data,None)
    
#     def get_length(self):
#         itr = self.head
#         count = 0
#         while itr:
#             count +=1
#             itr = itr.next
#         return count
    
#     def insert_at(self,index,ins_d):
#         if index < 0 or index > self.get_length():
#             raise Exception('invalid index')
#         if index == 0:
#             self.insert_frist(ins_d)
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
            
#     def inser_after_val(self,data,ins_d):
#         if self.head is None:
#             return None
#         if self.head.data == data:
#             self.head.next = Node(ins_d,self.head.next)
#             return
#         itr = self.head
#         while itr:
#             if itr.data == data:
#                 node = Node(ins_d,itr.next)
#                 itr.next  = node
#                 break
#             itr = itr.next
            
            
#     def print(self):
#         if self.head is None:
#             return
#         itr = self.head
#         listr = ''
#         while itr:
#             listr += str(itr.data) + '-->'
#             itr = itr.next
#         print(listr)
        
#     def delete_frist(self):
#         if self.head is None:
#             return None
#         data = self.head.data
#         self.head = self.head.next
#         return data
        
#     def delete_at(self,index):
#         if index < 0 or index > self.get_length():
#             raise Exception('invalid index')
#         if index == 0:
#             self.head = self.head.next
#         itr = self.head
#         count = 0
#         while itr:
#             if count == index -1:
#                 itr.next = itr.next.next
#             itr = itr.next
#             count += 1     

# if __name__ == '__main__':
#     li = SLL()
#     li.insert_frist(89)
#     li.insert_frist(78)
#     li.insert_last(1)
#     li.insert_last(2)
#     li.inser_after_val(2,34)
#     li.insert_at(0,43)
#     # li.delete_frist()
#     li.delete_at(0)
#     li.print()
    
    
    
# class Stack:
#     def __init__(self):
#         self.mylist = SLL()
#     def is_empty(self):
#         return self.mylist == None
#     def push_data(self,data):
#         self.mylist.insert_frist(data)
#     def pop_data(self):
#         if not self.is_empty():
#             return self.mylist.delete_frist()
#     def peek_data(self):
#         if not self.is_empty():
#             return self.mylist.head.data
#     def size(self):
#         if not self.is_empty():
#             return self.mylist.get_length()


# s1 = Stack()
# s1.push_data(89)
# s1.push_data(78)
# s1.push_data(7)
# print(s1.size())
# print(s1.peek_data())
# # print(s1.pop_data())
# # print(s1.size())
    
 
# Day ------------------------------5.)



# class Stack(SLL):
#     def __init__(self):
#         super().__init__()
#     def is_empty(self):
#         return self == None
#     def push_data(self,data):
#         self.insert_frist(data)
#     def pop_data(self):
#         if not self.is_empty():
#             return self.delete_frist()
#         raise Exception('There are no element')
#     def peek_data(self):
#         if not self.is_empty():
#             return self.head.data
#         raise Exception('There are no elemtet')
#     def size(self):
#         return self.get_length()
    
# s1 = Stack()
# s1.push_data(8)
# s1.push_data(6)
# s1.push_data(4)
# s1.push_data(56)
# print(s1.size())
# print(s1.pop_data())
# print(s1.peek_data())


