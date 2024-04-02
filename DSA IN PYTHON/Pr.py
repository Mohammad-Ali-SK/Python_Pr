class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next
class Linkedlist:
    def __init__(self):
        self.head = None
    
    def inser_at_b(self,data):
        node = Node(data,self.head)
        self.head = node
    
    def print(self):
        if self.head is None:
            print('Linked list is empty.')
            return
        itr = self.head
        listr = ''
        while itr:
            listr  += str(itr.data) + '-->'
            itr = itr.next
        print(listr)
        
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
        
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    def list_values(self,list_data):
        for i in list_data:
            self.insert_at_end(i)
    
    def remove_at(self,index):
        if index<0 or index>=self.get_length():
            raise Exception('invalid index')
        if index == 0:
            self.head = self.head.next
            return
        itr = self.head
        count = 0
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
            
    def insert_at(self,index,data):
        if index<0 or index>=self.get_length():
            raise Exception('i index')
        if index == 0:
            self.inser_at_b(data)
            return
        itr = self.head
        count = 0
        while itr:
            if count == index -1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1
        
    
        
        
        
        
        
        
        
        
        
        

if __name__  == '__main__':
    li = Linkedlist()
    li.inser_at_b(89)
    li.inser_at_b(8)
    # li.print()
    li.insert_at_end(8)
    li.insert_at_end(1)
    li.insert_at_end(12)
    li.list_values(['Alil','Amir','Rohit','Sumon'])
    print(li.get_length())
    li.print()
    # li.remove_at(0)
    li.insert_at(0,9888)
    li.print()