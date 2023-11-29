class Graph:
    def __init__(self,edges) -> None:
        self.edges = edges
        self.graph_dict = {}
        for start , end in edges:
            if start not in self.graph_dict:
                self.graph_dict[start] = [end]
            else:
                self.graph_dict[start].append(end)

        print(self.graph_dict)


    def get_paths(self, start, end, path=[]):
        path = path + [start]
        if start==end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths    


flight_routes = [
    ("Mumbai", "Lucknow"),
    ("Mumbai", "New York"),
    ("New York", "Mumbai"),
    ("New York", "Tokyo"),
    ("Mumbai", "Tokyo"),
    ("Tokyo", "New York")

]

flightGraph = Graph(flight_routes)

print(flightGraph.get_paths("Mumbai", 'Tokyo'))