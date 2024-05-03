# class Deque:
#     def __init__(self):
#         self.items = []
#     def is_empty(self):
#         return len(self.items) == 0
#     def insert_front(self,data):
#         self.items.insert(0,data)
#     def insert_rear(self,data):
#         self.items.append(data)
#     def delete_front(self):
#         if self.is_empty():
#             raise IndexError('No item here to delete.')
#         else:
#             self.items.pop(0)
#     def delete_rear(self):
#         if self.is_empty():
#             raise IndexError('No item ')
#         else:
#             self.items.pop()
#     def get_front(self):
#         if self.is_empty():
#             raise IndexError('DQ is empty.')
#         else:
#             return self.items[0]
#     def get_rear(self):
#         if self.is_empty():
#             raise IndexError('Dq is empty.')
#         else:
#             return self.items[-1]
        
#     def size(self):
#         return len(self.items)
    
# dq = Deque()
# dq.insert_front(8)
# dq.insert_front(7)
# dq.insert_rear(9)
# dq.insert_rear(10)
# print(dq.get_front(),dq.get_rear(),dq.size())



# *****Deque using Doubly Linked list concept******-------------------------------

# class Node:
#     def __init__(self,data= None, prev = None, next = None):
#         self.prev = prev
#         self.data = data
#         self.next = next

# class Deque:
#     def __init__(self):
#         self.front = None
#         self.rear = None
#         self.items_count = 0
        
#     def is_empty(self):
#         return self.items_count == 0
    
#     def insert_front(self,data):
#         node = Node(data,None,self.front)
#         if self.is_empty():
#             self.rear = node
#         else:
#             self.front.prev = node
#         self.front = node
#         self.items_count += 1
    
#     def insert_rear(self,data):
#         node = Node(data,self.rear)
#         if self.is_empty():
#             self.front = node
#             # self.rear = node
#         else:
#             self.rear.next = node
#         self.rear = node
#         self.items_count += 1
        
#     def delete_front(self):
#         if self.is_empty():
#             return None
#         if self.front == self.rear:
#             self.front = None
#             self.rear = None
#         else:
#             self.front = self.front.next
#             self.front.prev = None
#         self.items_count -= 1
            
#     def delete_rear(self):
#         if self.is_empty():
#             raise IndexError('no item is here')
#         if self.front == self.rear:
#             self.front = None
#             self.rear = None
#         else:
#             self.rear = self.rear.prev
#             self.rear.next = None
#         self.items_count -= 1
            
#     def get_front(self):
#         if self.is_empty():
#             raise IndexError('N I H')
#         else:
#             return self.front.data
#     def get_rear(self):
#         if self.is_empty():
#             raise IndexError('N I H')
#         else:
#             return self.rear.data
#     def print(self):
#         if self.is_empty():
#             raise IndexError('N I H')
#         itr = self.front
#         listr = ' '
#         while itr:
#             listr += str(itr.data) + '-->'
#             itr = itr.next
#         print(listr)
#     def size(self):
#         return self.items_count
        
    
# li = Deque()
# li.insert_front(8)
# li.insert_front(7)
# li.insert_front(6)
# li.insert_rear(9)
# li.insert_rear(10)
# print(li.get_front(),li.get_rear())
# li.delete_front()
# print(li.get_front(),li.get_rear())
# print(li.size())
# li.print()

class Node:
    def __init__(self,data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next
class Dq():
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0
    def is_empty(self):
        return self.item_count == 0
    
    def insert_front(self,data):
        node = Node(data,None,self.front)
        if self.is_empty():
            self.rear = node
        else:
            self.front.prev = node
        self.front = node
        self.item_count += 1
    
    #     def insert_front(self,data):
#         node = Node(data,None,self.front)
#         if self.is_empty():
#             self.rear = node
#         else:
#             self.front.prev = node
#         self.front = node
#         self.items_count += 1
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    def insert_rear(self,data):
        node = Node(data,self.rear)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            self.rear.next  = node
            self.rear = node
        self.item_count += 1
    
    def delete_front(self):
        if self.is_empty():
            raise IndexError('N I H')
        if self.front == self.rear:
            self.front = None
            self.rear =  None
        else:
            self.front = self.front.next
            self.front.next.prev = None
        self.item_count -= 1
        
    def delete_rear(self):
        if self.is_empty():
            raise IndexError('N I H')
        if self.front == self.rear:
            self.front = None
            self.rear =  None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.item_count -= 1
    def get_front(self):
        if self.is_empty():
            raise IndexError('N I H')
        else:
            return self.front.data
    def get_rear(self):
        if self.is_empty():
            raise IndexError('N O H')
        else:
            return self.rear.data
    
    def print(self):
        if self.is_empty():
            raise IndexError('J O L')
        itr = self.front
        listr = ''
        while itr:
            listr += str(itr.data) + '-->'
            itr = itr.next
        print(listr)



li = Dq()
li.insert_front(9)
li.insert_front(8)
li.insert_front(7)
li.insert_rear(10)
li.insert_rear(11)
li.insert_rear(12)
# li.delete_front()
# li.delete_rear()
li.print()
print(li.get_front(),li.get_rear())
