'''
Question1: Create a class to represent a graph as an adjacency list.
Question2: Write a function to add an edge to a graph represented as an adjacency list.
Question3: Write a function to remove an edge from a graph represented as an adjacency list.
Question4: Represent a graph as an adjacency matrix.
Question5: Implement breadth-first search (BFS) given a source node in a graph represented by an adjacency list.
Question6: Write a program that checks if all the nodes in a graph are connected.
Question7: Write a function that returns the list of connected components in a graph.
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

    # Adjacency matrices that represent graphs are symmetric (meaning they are equal to their transpose) so technically we did not need to transpose it.
    def __repr__(self):
        return "\n".join(["{}:{}".format(n, row) for n, row in enumerate(transpose(self.data))])

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

def bfs(graph, root):
    '''
    Description: Performs breadth-first search on a graph represented by an adjacency list.
    Input:
    graph: instance of Graph class.
    root:  a node in the graph representing the starting point for the search.
    
    Output:
    queue:    a list of discovered nodes in breadth-first fashion starting from the root node.
    distance: a list of distances from the root for all discovered nodes.
    parent:   a list of parent nodes for each discovered nodes.
    '''
    # Queue to keep the discovered but unexplored nodes.
    queue = []

    # List of booleans representing the discover/undiscovered status of nodes.
    discovered = [False] * len(graph.data)

    # List of distances from root to each node of the graph.
    distance = [None] * len(graph.data)

    # List of parents for each node (parent = the node that led to the discovery of the current node).
    parent = [None] * len(graph.data)

    discovered[root] = True
    distance[root] = 0
    queue.append(root)
    
    # The root node has no parent.
    parent[root] = None

    # Index in the queue list to dequeue from. 
    idx = 0

    while idx < len(queue):
        
        # Dequeue operation.
        # We could actually remove the first element from the list by doing queue.pop(0) but then we need to add it to another list in order to return the discovered nodes.
        current = queue[idx]
        idx += 1
        
        # Check all edges of current.
        for node in graph.data[current]:
            if not discovered[node]:
                
                # For each undiscovered node, the distance is 1 + the distance of the current node (which caused it to be discovered).
                discovered[node] = True
                distance[node] = 1 + distance[current]
                parent[node] = current
                queue.append(node)
    return queue, distance, parent

def connected_components(graph):
    '''
    Description: Returnes the list of connected components in a graph represented by an adjacency list.
    '''
    connected_components = []
    
    # List of undiscovered nodes. All nodes are undiscovered initially.
    undiscovered = [n for n in range(graph.num_nodes)]

    while len(undiscovered) > 0:
        
        # Get the first undiscovered node.
        root = undiscovered[0]
        
        # The discovered nodes returned by BFS from an undiscovered node represent a connected component.
        discovered = bfs(graph, root)[0]    
        connected_components.append(discovered)

        # Remove the discovered nodes from the undiscovered list.
        for node in discovered:
            undiscovered.remove(node)

    return connected_components

num_nodes1=5
edges1=[(0,1), (0,4), (1,2), (1,3), (1,4), (2,3), (3,4)]

graph1=GraphList(num_nodes1, edges1)

# print(bfs(graph1, 3))

# Example of a graph where not all nodes are connected.
num_nodes2=9
edges2=[(0,1), (0,3), (1,2), (2,3), (4,5), (4,6), (5,6), (7,8)] 
graph2=GraphList(num_nodes2, edges2)

# If all nodes in a graph are connected when you do a BFS traversal from any source you get to visit all nodes.
# Simply checking the length of the queue returned by bfs(graph, source) will determine whether or not all nodes are connected.
discovered = len(bfs(graph2, 0)[0])

print(graph2)

print(bfs(graph2, 0))

if discovered == graph2.num_nodes:
    print('All nodes are connected.')
else:
    print('All nodes are NOT connected')

connected_components = connected_components(graph2)
print(connected_components)
