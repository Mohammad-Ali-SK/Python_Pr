# # What is a Queue ?
# # Queue is a linear data structure
# # Working principle of Queue is ---- First in First out (FIFO)
 
 
# class Queue:
#     def __init__(self):
#         self.list = []
#     def is_empty(self):
#         return self.list == 0
#     def enqueue(self,data):
#         self.list.append(data)
#     def denqueue(self):
#         if not self.is_empty():
#             self.list.pop(0)
#     def get_front(self):
#         if not self.is_empty():
#             return self.list[0]
#     def get_last(self):
#         if not self.is_empty():
#             return self.list[-1]
#     def size(self):
#         return len(self.list)
    
# s1 = Queue()
# s1.enqueue(78)
# s1.enqueue(7)
# s1.enqueue(5)
# print(s1.size())
# # print(s1.get_front())
# print(s1.get_last())
# print(s1.get_last())
