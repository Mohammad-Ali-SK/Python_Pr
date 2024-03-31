class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None
        
    def insert_at_b(self,data):
        node = Node(data,self.head)
        self.head = node
        
    def print(self):
        if self.head is None:
            print('Linked list is empty.')
            return
        itr = self.head
        listr = ''
        while itr:
            listr += str(itr.data) + '-->'
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
    
    
    
    def list_val(self,list_data):
        for i in list_data:
            self.insert_at_end(i)
            
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    
    def remove_at(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception('invalid index.')
        
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
            raise Exception('invalid index.')
        if index == 0:
            self.insert_at_b(data)
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
    
    
    def insert_a_d(self,data,in_d):
        if self.head is None:
            return
        if self.head.data == data:
            self.head.next = Node(in_d,self.head.next)
            return
        itr = self.head
        while itr:
            if itr.data == data:
                itr.next = Node(in_d,itr.next)
                break
            itr = itr.next
    
    def remove_val(self,data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next


if __name__ == '__main__':
    li = Linkedlist()
    li.insert_at_b(0)
    li.insert_at_b(78)
    li.insert_at_end(88)
    li.insert_at_end(45)
    li.list_val(['Amir','Rohit','Roj','Sumi', 'Chhoto'])
    print(li.get_length())
    li.print()
    # li.remove_at(1)
    # li.insert_at(4,900)
    # li.inser_after_data('Amir','Ali')
    li.insert_a_d(0,8000)
    li.remove_val('Roj')
    li.print()