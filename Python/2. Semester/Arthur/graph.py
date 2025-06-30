from collections import defaultdict

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree():
    A = TreeNode("A")
    B = TreeNode("B")
    C = TreeNode("C")
    D = TreeNode("D")
    E = TreeNode("E")
    F = TreeNode("F")


    A.right = C
    A.left = B
    B.left = D
    B.right = E
    C.right = F

def tree_2_graph(root):
    graph = defaultdict(list)

    # Get understanding of DFS
    def dfs(node):
        if node is None:
            return
        if node.left: # This node return true
            graph[node.value].append(node.value.left)
            graph[node.left].append(node.value)
        if node.right:
            graph[node.value].append(node.value.right)
            graph[node.right].append(node.value)
    return graph

# Traversing through the graph
# def traverse_graph()