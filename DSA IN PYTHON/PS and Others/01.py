# Big O notion is used to measure how runing time or space requirments for your program grow as input size grows.

# def get_squr_numb(numb):
#     squared_numbers = []
#     for n in numb:
#         squared_numbers.append(n*n)
#     return squared_numbers

# numbers = [2,4,5,6]
# print(get_squr_numb(numbers))


# How to find dubicate number in python-----

# numbers = [3,6,2,4,3,6,8,9]

# for i in range(len(numbers)):
#     for j in range(i+1, len(numbers)):
#         if numbers[i] == numbers[j]:
#             print(numbers[i] , "is a duplicate")
#             break



# Common Complexities-------------------------------------
# 1. O(1) Constant
# 2. O(n) linear
# 3. O(n2) Quadratic
# 4. O(log n)
# 5. O(nlogn)
# 6. O()


# DSA Question in python______

# Arrays - Data Structures & Algorithms Tutorials in Python #3 --------------------#3

# exp = [2200,2350,2600,2130,2190]

# print(exp[1] - exp[0])
# print(exp[0] + exp[1] + exp[2])
# print(2000 in exp)
# exp.append(1980)
# print(exp)
# heros=['spider man','thor','hulk','iron man','captain america']
# print(len(heros))
# heros.append('black Panther')
# print(heros)
# heros.insert(3,'Blackpanther')
# print(heros)
# heros[1:3] = ['dr strange']
# print(heros)


# n = int(input('Enter the number___'))
# a = []
# for i in range(1,n+1):
#     if i%2 == 1:
#         a.append(i)
# print(a)



# Linked List - Data Structures & Algorithms Tutorials in Python #4-----------------------#4


class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next
        
        
class LinkedinList:
    def __init__(self):
        self.head = None
        
        
if __name__ == '__main__':
    pass


