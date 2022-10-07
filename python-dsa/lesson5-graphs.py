'''
Question1: Create a class to represent a graph as an adjacency list.
Question2: Write a function to add an edge to a graph represented as an adjacency list.
Question3: Write a function to remove an edge from a graph represented as an adjacency list.
Question4: Represent a graph as an adjacency matrix.
Question5: Implement breadth-first search (BFS) given a source node in a graph represented by an adjacency list.
Question6: Write a program that checks if all the nodes in a graph are connected.
Question7: Write a function that returns the list of connected components in a graph.
Question8: Implement depth-first search (DFS) given a source node in a graph represented by an adjacency list.
Question9: Create a class to represent weighted and directed graphs.
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

class GraphWD:
    def __init__(self, num_nodes, edges, directed=False):
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)]

        # Determine if the graph is weighted by checking the length of the first edge.
        weighted = (len(edges[0]) == 3) # True for weighted graphs.

        if weighted:
            for n1, n2, w in edges:
                self.data[n1].append((n2,w))
                if not directed:
                    self.data[n2].append((n1,w))
        else:
            for n1, n2 in edges:
                self.data[n1].append(n2)
                if not directed:
                    self.data[n2].append(n1)
    def __repr__(self):
       return "\n".join(["{}:{}".format(node, neighbors) for node, neighbors in enumerate(self.data)])

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

def dfs_iterative(graph, root):
    '''
    Description: Performs iterative depth-first search on a graph represented by an adjacency list.
    Input:
    graph: instance of Graph class.
    root:  a node in the graph representing the starting point for the search.
    
    Output:
    discovered_nodes: a list of discovered nodes in depth-first fashion starting from the root node.
    '''
    # Use a list as a stack structure.
    stack = []
    
    # List of discovered nodes.
    discovered_nodes = []
    
    # List of booleans that indicates whether each node is discovered.
    discovered = [False] * len(graph.data)
    
    stack.append(root)
    
    while len(stack) > 0:
        
        current = stack.pop()
        
        if not discovered[current]:
            discovered[current] = True
            discovered_nodes.append(current)
        
            # Check all edges of current.
            for node in graph.data[current]:        
                if not discovered[node]:
                    stack.append(node)
                
    return discovered_nodes

def dfs_recursive(graph, root, discovered=[]):
    '''
    Description: Performs recursive depth-first search on a graph represented by an adjacency list.
    Algorithm (Wikipedia):
    procedure DFS(G, v) is
        for all directed edges from v to w that are in G.adjacent.Edges(v) do
            if vertex w is not labeled as discovered then
                recursively call DFS(G, w)
    Credits: https://favtutor.com/blogs/depth-first-search-python
    '''

    if root not in discovered:
        discovered.append(root)

        for neighbor in graph.data[root]:
            dfs_recursive(graph, neighbor, discovered) 

    return discovered

def update_distances(graph, current, distance, parent=None):
    """Update the distances of the current node's neighbors"""

    neighbors = [graph.data[current][n][0] for n in range(len(graph.data[current]))]
    weights = [graph.data[current][n][1] for n in range(len(graph.data[current]))]
    
    for i, node in enumerate(neighbors):
        weight = weights[i]
        if distance[current] + weight < distance[node]:
            distance[node] = distance[current] + weight
            if parent:
                parent[node] = current

def pick_next_node(distance, visited):
    """Pick the next univisited node at the smallest distance"""

    min_distance = float('inf')
    min_node = None
    for node in range(len(distance)):
        if not visited[node] and distance[node] < min_distance:
            min_node = node
            min_distance = distance[node]
    return min_node

def shortest_path(graph, source, target):
    """Uses the Dijkstra's algorithm to find the shortest path between a source and a target node in a graph."""
    
    visited = [False] * graph.num_nodes 
    distance = [float('inf') for _ in range(graph.num_nodes)]
    queue = []
     
    distance[source] = 0
    queue.append(source)
    idx = 0
    
    while idx < len(queue) and not visited[target]:
        current = queue[idx]
        idx += 1             
        visited[current] = True
        
        # Update the distances of all the neighbors.
        update_distances(graph, current, distance)
    
        # Find the first unvisited node with the smallest distance.
        next_node = pick_next_node(distance, visited)
        if next_node:
            queue.append(next_node)
    
    return distance[target]

num_nodes1=5
edges1=[(0,1), (0,4), (1,2), (1,3), (1,4), (2,3), (3,4)]

graph1=GraphList(num_nodes1, edges1)

# print(bfs(graph1, 3))

# Example of a graph where not all nodes are connected.
# num_nodes2=9
# edges2=[(0,1), (0,3), (1,2), (2,3), (4,5), (4,6), (5,6), (7,8)] 
# graph2=GraphList(num_nodes2, edges2)

# Another graph
num_nodes3=10
edges3=[(0,1), (0,2), (0,3), (1,4), (2,5), (2,6), (3,7), (4,8), (5,9)]
# If all nodes in a graph are connected when you do a BFS traversal from any source you get to visit all nodes.
# Simply checking the length of the queue returned by bfs(graph, source) will determine whether or not all nodes are connected.
# discovered = len(bfs(graph2, 0)[0])

# print(graph2)

# print(bfs(graph2, 0))

# if discovered == graph2.num_nodes:
#     print('All nodes are connected.')
# else:
#     print('All nodes are NOT connected')

# connected_components = connected_components(graph2)
# print(connected_components)

# print(dfs_iterative(graph1,3))
# print(dfs_recursive(graph1,3))

# graph3=GraphList(num_nodes3, edges3)
# print(graph3)
# print(dfs_recursive(graph3,0))

# Graph with weights.
num_nodes5 = 9
edges5 = [(0, 1, 3), (0, 3, 2), (0, 8, 4), (1, 7, 4), (2, 7, 2), (2, 3, 6), 
          (2, 5, 1), (3, 4, 1), (4, 8, 8), (5, 6, 8)]

graph5 = GraphWD(num_nodes5, edges5)
print(graph5)

# Directed graph with weights.
num_nodes6 = 6
edges6 = [(0,1,4), (0,2,2), (1,2,5), (1,3,10), (2,4,3), (3,5,11), (4,3,4)]
directed6 = True

graph6 = GraphWD(num_nodes6, edges6, directed6)
print(graph6)

print(f"The shortest distance from 0 to 5 is:",shortest_path(graph6, 0, 5))
