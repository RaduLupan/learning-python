'''
Question: Create a class to represent a graph as an adjacency list.
'''

class Graph:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        
        # List of empty lists.
        self.data = [[] for _ in range(num_nodes)] 

        # Each edge shows in two lists corresponding to the two nodes it connects.
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
 
    def __repr__(self):
       return "\n".join(["{}:{}".format(node, neighbors) for node, neighbors in enumerate(self.data)])

num_nodes=5
edges=[(0,1), (0,4), (1,2), (1,3), (1,4), (2,3), (3,4)]

graph=Graph(num_nodes, edges)

print(graph.data)
print(repr(graph))
