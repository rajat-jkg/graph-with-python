class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start,end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
    
    def bfs_all_nodes(self, start):
        # BFS algorithm
        # BFS algorithm uses Queue data structure for finding the shortest path.
        queue = [start]
        visited = [start]
        queue+=self.graph_dict[start]
        while queue:
            try:
                node = queue.pop(0)
                if node not in visited:
                    visited.append(node)
                    queue+=self.graph_dict[node]
            except KeyError:
                continue
        return visited


flightRoutes = [
    ("Mumbai", "Paris"),
    ("Mumbai", "Dubai"),
    ("Paris", "Dubai"),
    ("Paris", "New York"),
    ("Dubai", "New York"),
    ("New York", "Toronto")
]

g1 = Graph(flightRoutes)

print(g1.bfs_all_nodes("Mumbai"))


