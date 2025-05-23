class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self,v):
        if v not in self.adj_list.keys():
            self.adj_list[v]=[]
            return True
        return False


my_graph = Graph()

my_graph.add_vertex('A')
my_graph.add_vertex('A')

my_graph.print_graph()



"""
    EXPECTED OUTPUT:
    ----------------
    A : []

"""