class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = edges

    def get_paths(self,start,end,path = []):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.get_paths(node, end, path)
                for p in new_path:
                    paths.append(p)
        return paths
    def get_shortest_path(self,start,end,path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in self.graph_dict:
            return None
        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node,end,path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path
    def dfs(self,start,visited=set()):
        if start not in self.edges:
            print(start, end=" ")
            visited.add(start)
            return
        if start not in visited:
            print(start,end=" ")
        visited.add(start)
        for i in self.edges[start] - visited:
            self.dfs(i,visited)
        return






if __name__ == "__main__":
    routes = {"Mumbai":{"Paris","Dubai"},"Paris":{"Dubai","New York"},"Dubai":{"New York"},"New York":{"Toronto"}}

    graph = Graph(routes)
    print(graph.graph_dict)
    print(graph.get_paths("Mumbai", "New York"))
    print(graph.get_shortest_path("Mumbai","New York"))
    graph.dfs("Mumbai")
