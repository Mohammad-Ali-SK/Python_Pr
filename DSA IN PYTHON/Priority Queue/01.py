
# class PriorityQueue:
#     def __init__(self):
#         self.items = []
    
#     def is_empty(self):
#         return len(self.items) == 0
#     def push(self,data,priority):
#         index = 0
        
#         while index < len(self.items) and self.items[index][1] <= priority:
#             index += 1
#         self.items.insert(index,(data,priority))
    
#     def pop(self):
#         if self.is_empty():
#             raise IndexError('N I I T')
#         return self.items.pop(0)[0]
#     def size(self):
#         return len(self.items)

# p = PriorityQueue()
# p.push('Amir',2)
# p.push('Eya',6)
# p.push('Kiron',4)
# p.push('Rup',3)
# p.push('Riya',1)

# while not p.is_empty():
#     print(p.pop())


