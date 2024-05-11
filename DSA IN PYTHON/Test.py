class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.graph_dist = {}
        for start,end in self.edges:
            if start in self.graph_dist:
                self.graph_dist[start].append(end)
            else:
                self.graph_dist[start] = [end]
    
    
    
    def get_path(self,start,end,path = []):
        path = path + [start]
        
        if start == end:
            return [path]
        if start not in self.graph_dist:
            return []
        
        paths = []
        for node in self.graph_dist[start]:
            if node not in path:
                new_paths = self.get_path(node,end,path)
                for p in new_paths:
                    paths.append(p)
        return paths
    
    
    
    def shortes_path(self,start,end,path=[]):
        path = path + [start]
        
        if start == end:
            return path
        
        if start not in self.graph_dist:
            return []
        
        sh_p = None
        for node in self.graph_dist[start]:
            if node not in path:
                sp = self.shortes_path(node,end,path)
                if sp:
                    if sh_p is None or len(sp) < len(sh_p):
                        sh_p = sp
        return sh_p
                        
    
    
    
    
    
    
    
if __name__ == "__main__":
    
    routs = [
        ("Mumbai","Paris"),
        ("Mumbai","Dubai"),
        ("Paris","Dubai"),
        ("Paris","New Yourk"),
        ("Dubai","New Yourk"),
        ("New Yourk","Kolkata"),
    ]
    
    g = Graph(routs)
    print(g.get_path("Mumbai","Kolkata"))
    print(g.shortes_path("Mumbai","Kolkata"))
    