from GraphWithHamiltonianPath import Graph
from GraphWithHamiltonianPath import Edge

class KnightTourModel:
    def __init__(self):
        # (u, v) is an edge if a knight can move from u and v
        edges = self.getEdges()

        # Create a graph with 64 vertices labeled 0 to 63
        self.graph = Graph(list(range(0, 64)), edges)

    # Get a Hamiltonian path starting from vertex v 
    def getHamiltonianPath(self, v):
        return self.graph.getHamiltonianPath(v)

    # Create edges for the graph 
    def getEdges(self):
        
        edges = [] # Store edges
        for i in range(0, 8):
            for j in range(0, 8):
                u = i * 8 + j # The vertex label
        
                # Check eight possible edges from u
                if i - 1 >= 0 and j - 2 >= 0:
                    v1 = (i - 1) * 8 + (j - 2)
                    edges.append([u, v1])
        
                if i - 2 >= 0 and j - 1 >= 0:
                    v2 = (i - 2) * 8 + (j - 1)
                    edges.append([u, v2])
        
                if i - 2 >= 0 and j + 1 <= 7:
                    v3 = (i - 2) * 8 + (j + 1);
                    edges.append([u, v3])
        
                if i - 1 >= 0 and j + 2 <= 7:
                    v4 = (i - 1) * 8 + (j + 2)
                    edges.append([u, v4])
        
                if i + 1 <= 7 and j + 2 <= 7:
                    v5 = (i + 1) * 8 + (j + 2)
                    edges.append([u, v5])
    
                if i + 2 <= 7 and j + 1 <= 7:
                    v6 = (i + 2) * 8 + (j + 1)
                    edges.append([u, v6])
        
                if i + 2 <= 7 and j - 1 >= 0:
                    v7 = (i + 2) * 8 + (j - 1)
                    edges.append([u, v7])
        
                if i + 1 <= 7 and j - 2 >= 0:
                    v8 = (i + 1) * 8 + (j - 2)
                    edges.append([u, v8])
    
        return edges
