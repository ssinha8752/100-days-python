class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        v_list = []
        for vertex in self.adj_list:
            v_list.append(vertex)
        v_list.sort()
        for v in v_list:
            print(v, ':', self.adj_list[v])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    ## WRITE ADD_EDGE METHOD HERE ##
    #                              #
    #                              #
    #                              #
    #                              #
    ################################




my_graph = Graph()

my_graph.add_vertex(1)
my_graph.add_vertex(2)

my_graph.add_edge(1,2)

my_graph.print_graph()



"""
    EXPECTED OUTPUT:
    ----------------
    1 : [2]
    2 : [1]

"""