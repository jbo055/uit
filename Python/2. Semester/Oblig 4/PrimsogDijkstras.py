from heapq import heappop, heappush

class Graph:
    def __init__(self, vertices=[], edges=[]):
        self._vertices = vertices if vertices else []
        self._neighbors = {vertex: [] for vertex in self._vertices}  # Adjacency list

        for edge in edges:
            if len(edge) == 3:  # Weighted edge (e.g., ('A', 'B', 5))
                self.add_edge(edge[0], edge[1], edge[2])

    def add_edge(self, from_vertex, to_vertex, weight=None):
        if from_vertex not in self._neighbors:
            self._neighbors[from_vertex] = []
        if to_vertex not in self._neighbors:
            self._neighbors[to_vertex] = []

        self._neighbors[from_vertex].append((to_vertex, weight))
        self._neighbors[to_vertex].append((from_vertex, weight))

    # Prim's Minimum Spanning Tree (MST)
    def prim_mst(self, start_node):
        visited = set() # hoder rede på besøkte noder
        mst_edges = []  # Vil holde kantene i MST (returverdi)
        total_weight = 0  # vil holde total vekt i MST (også returverdi)
        min_heap = []  # Prioritetskø for å velge den minste kanten
        visit_order = []  # Ny liste for besøksrekkefølge

        visited.add(start_node) # Marker startnode som besøkt
        visit_order.append(start_node) # Legger til startnode i besøksrekkefølge
        # Legg alle kanter fra startnode inn i prioritetskøen (vekt, fra, til)
        for neighbor, weight in self._neighbors[start_node]: # finn  naboer via nabolista
            if weight is not None:  # Only consider weighted edges
                heappush(min_heap, (weight, start_node, neighbor)) # legg alle kanter i prioritetskøen
               
        while min_heap:
            weight, from_vertex, to_vertex = heappop(min_heap) # Hent den minste kanten
           
            if to_vertex not in visited:
                # ..da legger vi til kanten i MST (det er den minste kanten)
                # ..og markerer den som besøkt
                visited.add(to_vertex)
                visit_order.append(to_vertex)
                mst_edges.append((from_vertex, to_vertex, weight)) # oppdaterer MST
                total_weight += weight # oppdaterer total vekt
                
                # Legg alle kanter fra to_vertex inn i prioritetskøen (vekt, fra, til)
                for neighbor, edge_weight in self._neighbors[to_vertex]:
                    if neighbor not in visited and edge_weight is not None:
                        heappush(min_heap, (edge_weight, to_vertex, neighbor))

        return mst_edges, total_weight, visit_order # visit_order er foreløpig dummy, bygg opp underveis

    # Dijkstra's Shortest Path Algorithm
    def dijkstra(self, start_node):
        distances = {vertex: float('inf') for vertex in self._vertices}
        distances[start_node] = 0
        parent_nodes = {vertex: None for vertex in self._vertices} # foreldrenoder, oppdateres underveis
        min_heap = [(0, start_node)]

        while min_heap:
            current_distance, current_node = heappop(min_heap)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self._neighbors[current_node]:
                if weight is not None:
                    new_distance = current_distance + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        parent_nodes[neighbor] = current_node  # Oppdaterer foreldrenode
                        heappush(min_heap, (new_distance, neighbor))

        paths = {} # dummy, bygg opp basert på parent_nodes
        for vertex in self._vertices:
            path = []
            current = vertex
            while current is not None:
                path.append(current)
                current = parent_nodes[current]
            path.reverse()
            paths[vertex] = path
        return distances, paths

vertices_small = ['A', 'B', 'C', 'D', 'E']
edges_small = [
    ('A', 'B', 1),
    ('A', 'C', 4),
    ('B', 'C', 2),
    ('B', 'D', 6),
    ('C', 'D', 3),
    ('C', 'E', 5),
    ('D', 'E', 2)
]
graph_small = Graph(vertices_small, edges_small)

# Apply Prim's MST on the small graph
mst_edges_small, total_weight_small, visit_order_small = graph_small.prim_mst('A')
print("Prim's MST (Small Graph):")
print("Edges:", mst_edges_small)
print("Total Weight:", total_weight_small)
print("Visit Order:", visit_order_small)

# Apply Dijkstra's algorithm on the small graph
distances_small, paths_small = graph_small.dijkstra('A')
print("\nDijkstra's Shortest Paths (Small Graph):")
print("Distances:", distances_small)
print("Paths:")
for vertex, path in paths_small.items():
    print(f"  {vertex}: {path}")

# Larger graph (from TestWeightedGraph.py)
vertices_large = ["Seattle", "San Francisco", "Los Angeles",
                  "Denver", "Kansas City", "Chicago", "Boston", "New York",
                  "Atlanta", "Miami", "Dallas", "Houston"]
edges_large = [
    ("Seattle", "San Francisco", 807), ("Seattle", "Denver", 1331), ("Seattle", "Chicago", 2097),
    ("San Francisco", "Seattle", 807), ("San Francisco", "Los Angeles", 381), ("San Francisco", "Denver", 1267),
    ("Los Angeles", "San Francisco", 381), ("Los Angeles", "Denver", 1015), ("Los Angeles", "Kansas City", 1663), ("Los Angeles", "Dallas", 1435),
    ("Denver", "Seattle", 1331), ("Denver", "San Francisco", 1267), ("Denver", "Los Angeles", 1015), ("Denver", "Kansas City", 599), ("Denver", "Chicago", 1003),
    ("Kansas City", "Los Angeles", 1663), ("Kansas City", "Denver", 599), ("Kansas City", "Chicago", 533), ("Kansas City", "New York", 1260),
    ("Kansas City", "Atlanta", 864), ("Kansas City", "Dallas", 496),
    ("Chicago", "Seattle", 2097), ("Chicago", "Denver", 1003), ("Chicago", "Kansas City", 533), ("Chicago", "Boston", 983), ("Chicago", "New York", 787),
    ("Boston", "Chicago", 983), ("Boston", "New York", 214),
    ("New York", "Kansas City", 1260), ("New York", "Chicago", 787), ("New York", "Boston", 214), ("New York", "Atlanta", 888),
    ("Atlanta", "Kansas City", 864), ("Atlanta", "New York", 888), ("Atlanta", "Miami", 661), ("Atlanta", "Dallas", 781), ("Atlanta", "Houston", 810),
    ("Miami", "Atlanta", 661), ("Miami", "Houston", 1187),
    ("Dallas", "Los Angeles", 1435), ("Dallas", "Kansas City", 496), ("Dallas", "Atlanta", 781), ("Dallas", "Houston", 239),
    ("Houston", "Atlanta", 810), ("Houston", "Miami", 1187), ("Houston", "Dallas", 239)
]
graph_large = Graph(vertices_large, edges_large)

# Apply Prim's MST on the large graph
mst_edges_large, total_weight_large, visit_order_large = graph_large.prim_mst("Seattle")
print("\nPrim's MST (Larger Graph):")
print("Edges:", mst_edges_large)
print("Total Weight:", total_weight_large)
print("Visit Order:", visit_order_large)

# Apply Dijkstra's algorithm on the large graph
distances_large, paths_large = graph_large.dijkstra("Seattle")
print("\nDijkstra's Shortest Paths (Larger Graph):")
print("Distances:", distances_large)
print("Paths:")
for vertex, path in paths_large.items():
    print(f"  {vertex}: {path}")
