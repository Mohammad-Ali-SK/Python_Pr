class Node:
    def __init__(self,data=None,next = None):
        self.data = data
        self.next = next
class Linkedlist:
    def __init__(self):
        self.head = None
    
    # Add element at the beginig___
    def insert_at_beg(self,data):
        node = Node(data,self.head)
        self.head = node
        
    def print(self):
        if self.head is None:
            print('Linkedlist  is empty....')
            return
        current = self.head
        listr = ''
        while current:
            listr += str(current.data) + '-->'
            current = current.next
        print(listr)
        
        
        # Insert element at the end from linkedlist______
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        current = self.head
        while current.next:
            current = current.next
            
        current.next = Node(data,None)
        
        
        
        # lisert list valuse at the linkedlist-------
    def list_value(self,data_list):
        for data in data_list:
            self.insert_at_end(data)
            
            
            # FInd length at the linkedlist_---------
    def get_length(self):
        count = 0
        current = self.head
        while current:
            count = count + 1
            current = current.next
        return  count
    
    


if __name__ == '__main__':
    li = Linkedlist()
    li.insert_at_beg(89)
    li.insert_at_beg(878)
    li.insert_at_end(8)
    li.list_value(['amir','soyel','sabir'])
    li.print()
    print(li.get_length())