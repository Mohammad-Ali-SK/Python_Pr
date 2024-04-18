# class Node:
#     def __init__(self,data = None, priority = None, next = None):
#         self.data = data
#         self.priority = priority
#         self.next = next
# class Priority:
#     def __init__(self):
#         self.head = None
#         self.item_count = 0
        
#     def is_empty(self):
#         return self.item_count == 0
    
#     def push(self,data,priority):
#         node = Node(data,priority)
#         if not self.head or priority < self.head.priority:
#             node.next = self.head
#             self.head = node
#         else:
#             itr = self.head
#             while itr.next and itr.next.priority <= priority:
#                 itr = itr.next
#             node.next = itr.next
#             itr.next = node
#         self.item_count += 1
        
#     def pop(self):
#         if self.is_empty():
#             raise IndexError('N I A H')
#         data = self.head.data
#         self.head = self.head.next
#         self.item_count -= 1
#         return data
#     def size(self):
#         return self.item_count

# p = Priority()
# p.push('Amir',2)
# p.push('Eya',6)
# p.push('Kiron',4)
# p.push('Rup',3)
# p.push('Riya',1)

# while not p.is_empty():
#     print(p.pop())

