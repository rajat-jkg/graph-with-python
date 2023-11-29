# this is a basic graph representation using dictionary
# it takes a list of tuples as input and creates a dictionary
class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start,end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]


# a graph can be represented as list of tuples. 
# Each tuple has two elements. 
# The first element is the starting node and the second element is the ending node of an edge.
flightRoutes = [
    ("Mumbai", "Paris"),
    ("Mumbai", "Dubai"),
    ("Paris", "Dubai"),
    ("Paris", "New York"),
    ("Dubai", "New York"),
    ("New York", "Toronto")
]


# creating a graph object
routes = Graph(flightRoutes)
# printing the graph dictionary
print(routes.graph_dict)