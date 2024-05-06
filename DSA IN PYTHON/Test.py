class Graph:
    def __init__(self,vno):
        self.vitrix_count = vno
        self.adj_matrix = [[0]*vno for i in range(vno)]
    
    
    def add_edge(self,u,v,weight = 1):
        if 0<=u<self.vitrix_count and 0<=v<self.vitrix_count:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight
        else:
            print('Invalid vitrix')
    
    def remove_vet(self,u,v):
        if 0<=u<self.vitrix_count and 0<=v<self.vitrix_count:
            self.adj_matrix[u][v] = 0
        else:
            print('Invalid vetrix...')
    def has_edge(self,u,v):
        if 0<=u<self.vitrix_count and 0<=v<self.vitrix_count:
            return self.adj_matrix[u][v] != 0
        else:
            print('invalid vetrix')
    
    def print_vet(self):
        for row_list in self.adj_matrix:
            print(" ".join(map(str,row_list)))

g = Graph()
g.add_edge(1,2)
g.add_edge(2,3)