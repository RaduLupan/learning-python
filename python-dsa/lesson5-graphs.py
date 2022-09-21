'''
Question1: Create a class to represent a graph as an adjacency list.
Question2: Write a function to add an edge to a graph represented as an adjancecy list.
Question3: Write a function to remove an edge from a graph represented as an adjancecy list.
Question4: Represent a graph as an adjacency matrix.
'''

class GraphList:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        
        # List of empty lists.
        self.data = [[] for _ in range(num_nodes)] 

        # Each edge shows in two lists corresponding to the two nodes it connects.
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
 
    def add_edge(self, n1, n2):
        
        # Brings the nodes within the Graph in case n1,n2 >= len(self.data)
        n1 = n1 % len(self.data)
        n2 = n2 % len(self.data)

        # Avoids adding the same edge multiple times.
        if n2 not in self.data[n1]:
            self.data[n1].append(n2)
        if n1 not in self.data[n2]:
            self.data[n2].append(n1)

    def remove_edge(self, n1, n2):

        # Brings the nodes within the Graph in case n1,n2 >= len(self.data)
        n1 = n1 % len(self.data)
        n2 = n2 % len(self.data)

        # Only removes existing edges.
        if n2 in self.data[n1]:
            self.data[n1].remove(n2)
        if n1 in self.data[n2]:
            self.data[n2].remove(n1)

    def __repr__(self):
       return "\n".join(["{}:{}".format(node, neighbors) for node, neighbors in enumerate(self.data)])

class GraphMatrix:
    def __init__(self, num_nodes, edges):
        self.num_nodes=num_nodes

        # Create an all-zero matrix.
        self.data = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]

        # Populate the elements of the matrix with 1s for each edge.
        for n1, n2 in edges:
            self.data[n1][n2]=1
            self.data[n2][n1]=1

    def __repr__(self):
        return "\t".join(["{}:{}".format(n, row) for n, row in enumerate(self.data)])

def transpose(matrix):
    '''
    Description: Computes the transpose of a matrix represented by a list of columns. Returns the flipped version of the matrix as a list of rows.
    Input:       A list of lists (representing columns).
    Output:      A list of lists (representing rows in the initial matrix).
    '''     
    # The number of columns in the matrix is equal with the length of the matrix represented as a list of columns.
    # The number of rows in the matrix is equal with the length of any list that represents a column.
    num_cols, num_rows = len(matrix), len(matrix[0]) 

    transposed_matrix = []

    for j in range(num_rows):
        element = [matrix[i][j] for i in range(num_cols)]
        transposed_matrix.append(element)
    
    return transposed_matrix

num_nodes=5
edges=[(0,1), (0,4), (1,2), (1,3), (1,4), (2,3), (3,4)]

graph=GraphMatrix(num_nodes, edges)
print(graph.data)

print(graph)
#graph.add_edge(0,3)
#print(graph)

#graph.remove_edge(0,3)
#print(graph)

#s=''
#for n, row in enumerate(m2):
#    s += "\n{}:{}".format(n, row)
