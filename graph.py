class Graph:
     def __init__(self,edges):
         self.edges = edges
         self.graph_dict= dict()
         for start,end,weight in self.edges:
            if start in self.graph_dict:
                 self.graph_dict[start].append([end,weight])
            else:
                self.graph_dict[start] = [[end,weight]]
     def get_paths(self,start,end,path=[]):
         path = path+[start]
         if start == end:
             return [path]
         if start not in self.graph_dict:
             return []
         paths = []
         for node in self.graph_dict[start]:
             if node[0] not in path:
                 new_path = self.get_paths(node[0],end,path)
                 for p in new_path:
                     paths.append(p)
         return paths
     def get_shortest_path(self,start,end,path = [],weights = 0): #for weighted graph,for directed graph ignore the weight param
         path = path + [start]
         sum = 0                #only for weighted graph
         sum = sum + weights    #only for weighted graph
         if start == end:
             return path,sum
         if start not in self.graph_dict:
             return None
         shortest_path = None
         min_weight = 0
         for node in self.graph_dict[start]:
             if node[0] not in path:            #ignore indexing for directed graph
                 sp,val = self.get_shortest_path(node[0],end,path,node[1]+sum)
                 if sp:
                     # if shortest_path is None or (len(sp) < len(shortest_path) : for directed graph
                     if (min_weight > val or shortest_path is None):
                         shortest_path = sp
                         min_weight = val
         return shortest_path,min_weight
if __name__=="__main__":
    routes = [
        ("Mumbai","Paris",20),
        ("Mumbai","Dubai",70),
        ("Paris","Dubai",30),
        ("Paris","New York",50),
        ("Dubai","New York",35),
        ("New York","Toronto",90)
    ]
    graph = Graph(routes)
    print(graph.get_paths("Mumbai","New York"))
    print(graph.get_shortest_path("Mumbai","New York"))