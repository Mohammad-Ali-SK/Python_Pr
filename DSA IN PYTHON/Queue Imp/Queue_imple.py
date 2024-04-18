# class Node:
#     def __init__(self,data = None,next = None):
#         self.data = data
#         self.next = next

# class Queue:
#     def __init__(self):
#         self.front = None
#         self.rear = None
#         self.item_count = 0
#     def is_empty(self):
#         return self.front == None
        
#     def enqueue(self,data):
#         node = Node(data)
#         if self.is_empty():
#             self.front = node
            
#         else:
#             self.rear.next = node
#         self.rear = node
#         self.item_count += 1
        
#     def dequeue(self):
#         if self.is_empty():
#             raise IndexError('Empty Queue')
#         elif self.front == self.rear:
#             self.front = None
#             self.rear = None
#         else:
#             self.front = self.front.next
            
#         self.item_count -= 1
        
#     def get_front(self):
#         if self.is_empty():
#             raise IndexError('Empty Queue.')
#         else:
#             return self.front.data
    
#     def get_rear(self):
#         if self.is_empty():
#             raise IndexError('Empty Queue')
#         else:
#             return self.rear.data
#     def size(self):
#         return self.item_count
    
# q1 = Queue()
# q1.enqueue(8)
# q1.enqueue(9)
# q1.enqueue(10)
# q1.dequeue()

# print(q1.get_front(),q1.get_rear(),q1.size())


class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.front  = None
        self.rear = None
        self.item_count = 0
    
    def is_empty(self):
        return self.item_count == 0
    
    def enqueue(self,data):
        node = Node(data)
        if self.is_empty():
            self.front = node
        else:
            self.rear.next = node
        self.rear = node
        self.item_count += 1
        
    def dequeue(self):
        if self.is_empty():
            return IndexError('There is no item')
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        self.item_count -= 1
        
    def get_front(self):
        if self.is_empty():
            return IndexError('There are no item in the stack')
        else:
            return self.front.data
    
    def get_rear(self):
        if self.is_empty():
            return IndexError('Empty stck')
        else:
            return self.rear.data
        
q1 = Queue()
q1.enqueue(9)
q1.enqueue(10)
q1.enqueue(11)
q1.enqueue(12)
print(q1.get_front(),q1.get_rear())