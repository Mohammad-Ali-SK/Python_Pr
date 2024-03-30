class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def insert_at_frist(self,data):
        node = Node(data,self.head)
        self.head = node
        
    def print(self):
        if self.head is None:
            print('Linked list is empty..')
            return
        current = self.head
        listr = ''
        while current:
            listr += str(current.data) + '-->'
            current =  current.next
            
        print(listr)
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        current = self.head
        while current.next:
            current = current.next
            
        current.next = Node(data,None)
        
    def insert_values(self,data_list):
        # self.head = None
        for i in data_list:
            self.insert_at_end(i)
        
        
    def get_length(self):
        count = 0
        current = self.head
        
        while current:
            count = count + 1
            current  = current.next
        return count
        
        
        
        
if __name__ == '__main__':
    li = Linkedlist()
    li.insert_at_frist(89)
    li.insert_at_frist(65)
    li.insert_at_end(12)
    li.insert_at_frist(89)
    li.insert_at_frist(65)
    li.insert_at_end(12)
    li.insert_values(['Amir','Rohit','KIron','ROj'])
    li.print()
    print(li.get_length())