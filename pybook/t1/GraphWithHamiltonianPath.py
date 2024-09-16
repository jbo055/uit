from Queue import Queue 

class Graph:
    def __init__(self, vertices = [], edges = []):
        self.vertices = vertices
        self.neighbors = self.getAdjacnecyLists(edges)

    # Return a list of adjacency lists for edges 
    def getAdjacnecyLists(self, edges):
        neighbors = []
        for i in range(len(self.vertices)):
            neighbors.append([]) # Each element is another list
            
        for i in range(len(edges)):
            u = edges[i][0]
            v = edges[i][1]
            neighbors[u].append(Edge(u, v)) # Insert an edge (u, v)

        return neighbors
    
    # Return the number of vertices in the graph 
    def getSize(self):
        return len(self.vertices)

    # Return the vertices in the graph 
    def getVertices(self):
        return self.vertices

    # Return the vertex at the specified index
    def getVertex(self, index):
        return self.vertices[index]

    # Return the index for the specified vertex 
    def getIndex(self, v):
        return self.vertices.index(v)

    # Return the neighbors of vertex with the specified index 
    def getNeighbors(self, index):
        return self.neighbors[index]
    
    # Return the degree for a specified vertex 
    def getDegree(self, v):
        return len(self.neighbors[self.getIndex(v)])

    # Print the edges 
    def printEdges(self):
        for u in range(0, len(self.neighbors)):
            print(str(self.getVertex(u)) + " (" + str(u), end = "): ")
            for j in range(len(self.neighbors[u])):
                print("(" + str(u) + ", " + 
                      str(self.neighbors[u][j].v), end = ") ")
            print()

    # Clear graph 
    def clear(self):
        vertices = []
        neighbors = []
  
    # Add a vertex to the graph   
    def addVertex(self, vertex):
        if not (vertex in self.vertices):
            self.vertices.append(vertex)
            self.neighbors.append([]) # add a new empty adjacency list
        
    # Add an undirected edge to the graph   
    def addEdge(self, u, v):
        if u in self.vertices and v in self.vertices:
            indexU = self.getIndex(u)
            indexV = self.getIndex(v)
            # Add an edge (u, v) to the graph
            self.neighbors[indexU].append(Edge(indexU, indexV))
  
    # Obtain a DFS tree starting from vertex u 
    # To be discussed in Section 22.6 
    def dfs(self, v):
        searchOrders = []
        parent = len(self.vertices) * [-1] # Initialize parent[i] to -1

        # Mark visited vertices
        isVisited = len(self.vertices) * [False]

        # Recursively search
        self.dfsHelper(v, parent, searchOrders, isVisited)

        # Return a search tree
        return Tree(v, parent, searchOrders, self.vertices)

    # Recursive method for DFS search 
    def dfsHelper(self, u, parent, searchOrders, isVisited):
        # Store the visited vertex
        searchOrders.append(u)
        isVisited[u] = True # Vertex v visited

        for e in self.neighbors[u]:
            if not isVisited[e.v]:
                parent[e.v] = u # The parent of vertex i is v
                # Recursive search
                self.dfsHelper(e.v, parent, searchOrders, isVisited) 

    # Starting bfs search from vertex v 
    # To be discussed in Section 22.7 
    def bfs(self, v):
        searchOrders = []
        parent = len(self.vertices) * [-1] # Initialize parent[i] to -1

        queue = Queue() # the Queue class is defined in Chapter 17
        isVisited = len(self.vertices) * [False]
        queue.enqueue(v) # Enqueue v
        isVisited[v] = True # Mark it visited

        while not queue.isEmpty():
            u = queue.dequeue() # Dequeue to u
            searchOrders.append(u) # u searched
            for e in self.neighbors[u]:
                if not isVisited[e.v]:
                    queue.enqueue(e.v) # Enqueue w
                    parent[e.v] = u # The parent of w is u
                    isVisited[e.v] = True # Mark it visited

        return Tree(v, parent, searchOrders, self.vertices)

    # Return a Hamiltonian path from the specified vertex object
    # Return null if the graph does not contain a Hamiltonian path 
    def getHamiltonianPath(self, vertex):
        return self.getHamiltonianPath2(self.getIndex(vertex))

    # Return a Hamiltonian path from the specified vertex label
    # Return null if the graph does not contain a Hamiltonian path 
    def getHamiltonianPath2(self, v):
        # A path starts from v. (i, next[i]) represents an edge in 
        # the path. isVisited[i] tracks whether i is currently in the 
        # path.
        next = self.getSize() * [-1] # Indicate no subpath from i is found yet
      
        isVisited = self.getSize() * [False] 
      
        # The vertices in the Hamiltonian path are stored in result
        result = []
        
        # To speed up search, reorder the adjacency list for each 
        # vertex so that the vertices in the list are in increasing 
        # order of their degrees
        for i in range(self.getSize()):
            self.reorderNeigborsBasedOnDegree(self.neighbors[i])
      
        if self.getHamiltonianPath3(v, next, isVisited):
            result = [] # Create a list for path        
            vertex = v; # Starting from v
            while vertex != -1:
                result.append(vertex) # Add vertex to the result list
                vertex = next[vertex] # Get the next vertex in the path
      
        return result # return empty list if no Hamiltonian path is found

    # Reorder the adjacency list in increasing order of degrees */
    def reorderNeigborsBasedOnDegree(self, list):
        for i in range(len(list) - 1, 0, -1): 
            # Find the maximum in the list[0..i]
            currentMaxDegree = self.getDegree(list[0].v)
            currentMaxIndex = 0
    
            for j in range(1, i + 1):
                if currentMaxDegree < self.getDegree(list[j].v): 
                    currentMaxDegree = self.getDegree(list[j].v)
                    currentMaxIndex = j
    
            # Swap list[i] with list[currentMaxIndex] if necessary
            if currentMaxIndex != i:
                temp = list[currentMaxIndex]
                list[currentMaxIndex] = list[i]
                list[i] = temp
    
    # Return true if all elements in array isVisited are true 
    def allVisited(self, isVisited):
        result = True
      
        for i in range(0, self.getSize()): 
            result = result and isVisited[i]
      
        return result   
    
    # Search for a Hamiltonian path from v 
    def getHamiltonianPath3(self, v, next, isVisited):
        isVisited[v] = True # Mark vertex v visited

        if self.allVisited(isVisited): 
            return True # The path now includes all vertices, thus found
        
        for i in range(0, len(self.neighbors[v])):
            u = self.neighbors[v][i].v
            if not isVisited[u] and self.getHamiltonianPath3(u, next, isVisited):
                next[v] = u # Edge (v, u) is in the path
                return True 

        isVisited[v] = False # Backtrack, v is marked unvisited now
        return False # No Hamiltonian path exists from vertex v
    
# Tree  class will be discussed in Section 22.5 
class Tree:
    def __init__(self, root, parent, searchOrders, vertices):
        self.root = root # The root of the tree
        # Store the parent of each vertex in a list
        self.parent = parent 
        # Store the search order in a list
        self.searchOrders = searchOrders 
        self.vertices = vertices # vertices of the graph

    # Return the root of the tree 
    def getRoot(self):
      return self.root

    # Return the parent of vertex v 
    def getParent(self, index):
        return self.parent[index]

    # Return an array representing search order 
    def getSearchOrders(self):
        return self.searchOrders

    # Return number of vertices found 
    def getNumberOfVerticesFound(self):
        return len(self.searchOrders)
    
    # Return the path of vertices from a vertex index to the root 
    def getPath(self, index):
        path = []

        while index != -1:
            path.append(self.vertices[index])
            index = self.parent[index]

        return path

    # Print a path from the root to vertex v 
    def printPath(self, index):
        path = self.getPath(index)
        print("A path from " + str(self.vertices[self.root]) + " to " 
              + str(self.vertices[index]), end = ": ")
        for i in range(len(path) - 1, -1, -1):
            print(path[i], end = " ")

    # Print the whole tree 
    def printTree(self):
        print("Root is: " + str(self.vertices[self.root]))
        print("Edges: ", end = "")
        for i in range(len(self.parent)):
            if self.parent[i] != -1:
                # Display an edge
                print("(" + str(self.vertices[self.parent[i]]) 
                      + ", " + str(self.vertices[i]), end = ") ")

        print()        
        
# The Edge class for defining an edge from u to v        
class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v
        
    def __str__(self):
        return "[" + str(self.u) + ", " + str(self.v) + "]"
