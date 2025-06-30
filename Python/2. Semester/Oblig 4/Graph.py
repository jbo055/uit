from collections import deque

class Graph:
    def __init__(self, vertices = None, edges = None):
        self.vertices = list(vertices) if vertices is not None else []
        self.neighbors = self.get_adjacencylists(edges if edges is not None else [])

    # Return a list of adjacency lists for edges 
    def get_adjacencylists(self, edges):
        neighbors = {v: [] for v in self.vertices} # Initialize empty lists for each vertex
        for (u, v) in edges:
            if u in neighbors and v in neighbors:
                neighbors[u].append(v)
        return neighbors
    
    # Return the number of vertices in the graph 
    def get_size(self):
        return len(self.vertices)

    # Return the vertices in the graph 
    def get_vertices(self):
        return self.vertices

    # Return the vertex at the specified index
    def get_vertex(self, index):
        return self.vertices[index]

    # Return the index for the specified vertex 
    def get_index(self, v):
        return self.vertices.index(v)

    # Return the neighbors of vertex with the specified index 
    def get_neighbors(self, index):
        return self.neighbors[index]
    
    # Return the degree for a specified vertex 
    def get_degree(self, v):
        return len(self.get_neighbors(v))

    # Print the edges 
    def print_edges(self):
        for u in self.vertices:
            for v in self.get_neighbors(u):
                print(f"({u}, {v})")
  
    # Add a vertex to the graph   
    def add_vertex(self, vertex):
        if not (vertex in self.vertices):
            self.vertices.append(vertex)
            self.neighbors[vertex] = [] # add a new empty adjacency list
        
    # Add an undirected edge to the graph   
    def add_edge(self, u, v):
        if u in self.neighbors and v in self.neighbors:
            self.neighbors[u].append(v)
  
    # Obtain a DFS tree starting from vertex u 
    # To be discussed in Section 22.6 
    def dfs(self, start_node):
        visited = {start_node}
        stack = deque([start_node])
        order = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)

                for neighbor in self.get_neighbors(node):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return order

    # Starting bfs search from vertex v 
    # To be discussed in Section 22.7 
    def bfs(self, start_node):
        visited = {start_node} # Bruker et sett for å holde styr på besøkte noder
        queue = deque([start_node]) # Bruker deque som kø
        order = [] # Liste for å holde besøksrekkefølgen

        while queue:
            node = queue.popleft() # popleft får queue til å oppføre seg som en kø
            order.append(node)
            for neighbor in self.get_neighbors(node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order
    
    def bfs_all_shortest_paths(self, start_node):
        visited = {start_node}
        queue = deque([start_node])
        paths = {start_node: [start_node]}
        while queue:
            node = queue.popleft()
            for neighbor in self.get_neighbors(node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    paths[neighbor] = paths[node] + [neighbor]
        return paths
    
    
    def is_connected(self):
        visited = set()
        queue = deque([self.vertices[0]])
        visited.add(self.vertices[0])
        while queue:
            node = queue.popleft()
            for neighbor in self.get_neighbors(node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return len(visited) == len(self.vertices)



cities = ["London", "Paris", "Berlin", "Madrid", "Rome", "Vienna", "Amsterdam", "Prague"]

edges = [
    ("London", "Madrid"),
    ("London", "Vienna"),
    ("London", "Prague"),
    ("London", "Paris"),
    ("Paris", "Madrid"),
    ("Berlin", "Prague"),
    ("Berlin", "Paris"),
    ("Rome", "London"),
    ("Rome", "Vienna"),
    ("Rome", "Prague"),
    ("Vienna", "Amsterdam"),
    ("Vienna", "Prague"),
    ("Vienna", "Madrid"),
    ("Vienna", "Paris"),
    ("Amsterdam", "Prague")
]

graph1 = Graph(cities, edges) # Create graph1
print("The vertices in graph1: " + str(graph1.get_vertices()))
print("The number of vertices in graph1: " + str(graph1.get_size()))

print("The degree for London is " + str(graph1.get_degree("London")))
print("The edges for graph1:")
graph1.print_edges()
    
print("adding a new vertex: Oslo")
graph1.add_vertex("Oslo") # Add a new vertex
print("Adding new edges: Oslo-London, Oslo-Paris")
graph1.add_edge("Oslo", "London")
graph1.add_edge("Oslo", "Paris")
print("\nThe edges for graph1 after adding a new vertex and 2 new edges:")
graph1.print_edges()

# test bfs
print("\nBFS traversal from London:")
bfs_result = graph1.bfs("London")  
print(bfs_result)
# test dfs
print("\nDFS traversal from London:")
dfs_result = graph1.dfs("London")
print(dfs_result)
# test is_connected
print("Is graph1 connected? " + str(graph1.is_connected()))

vertice2 = ['A', 'B', 'C', 'D', 'E']
edges2 = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'D'), ('C', 'E'), ('D', 'E')]
graph2 = Graph(vertice2, edges2) # Create graph2
print("\nThe vertices in graph2: " + str(graph2.get_vertices()))
print("The number of vertices in graph2: " + str(graph2.get_size()))
print("The degree for A is " + str(graph2.get_degree("A")))
print("The edges for graph2:")
graph2.print_edges()
print("Is graph2 connected? " + str(graph2.is_connected()))
print("\nBFS traversal from A:")
bfs_result = graph2.bfs("A")
print(bfs_result)
print("\nBFS (all shortest path) traversal from A:")
bfs_result = graph2.bfs_all_shortest_paths("A")
print(bfs_result)
print("\nDFS traversal from A:")
dfs_result = graph2.dfs("A")
print(dfs_result)

# Removed unused methods: dfsHelper and clear