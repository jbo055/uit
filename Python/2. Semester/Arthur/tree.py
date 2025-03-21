class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def insert(self, value, node = None):
        if node is None: # If we do not have a value
            node = self.root
        if value < node.value: # If this value is smaller than the current value
            if node.left is None: # If there is no child to the left
                node.left = TreeNode(value)
            else: # If there is a child to the left
                self.insert(value, node.left)
        else: # If this value is larger than or equal to the current value
            if node.right is None: # If there is no child to the right
                node.right = TreeNode(value)
            else: # If there is a child to the right
                self.insert(value, node.right)


    def traverse(self, node = None):
        # In-order traversal
        if node is None: # If no node was sent as a parameter to the method traverse
            node = self.root # We set the non existing node to the main root
        if node.left:
            self.traverse(node.left)
        print(node.value)
        if node.right:
            self.traverse(node.right)

binarytree = BinaryTree(10)
binarytree.insert(5)
binarytree.insert(15)

binarytree.traverse() # 5, 10, 15