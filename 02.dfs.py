class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start,end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

    def dfs_all_nodes(self, start, visited=[]):
        # DFS algorithm
        # DFS algorithm uses Stack data structure for finding the shortest path.
        try:
            visited.append(start)
            for x in self.graph_dict[start]:
                if x not in visited:
                    self.dfs_all_nodes(x,visited)
        except KeyError:
            pass
        return visited
    


flightRoutes = [
    ("Mumbai", "Paris"),
    ("Mumbai", "Dubai"),
    ("Paris", "Dubai"),
    ("Paris", "New York"),
    ("Dubai", "New York"),
    ("New York", "Toronto")
]

g2 = Graph(flightRoutes)

print(g2.dfs_all_nodes("Mumbai"))
