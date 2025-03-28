class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value): # Revursion is a main component in the insert method
        # If we do not have a node, we create a new node and assign it to the root
        if self.root is None:
            self.root = Node(value)
        # Or we call the insert function again to insert the data
        else: # Insert data recursively
            self.insert_recursively(self.root, value)

    def insert_recursively(self, current_node, value): # We want to insert the data in the correct position
        if value < current_node.value: # If our value is smaller than the current node, we go to the left
            if current_node.left is None: # If our left node is empty, we create a new node
                current_node.left = Node(value)
            else:
                self.insert_recursively(current_node.left, value)
        
        elif value > current_node.value: # If our value is greater than the current node, we go to the right
            if current_node.right is None: # If our right node is empty, we create a new node
                current_node.right = Node(value)
            else:
                self.insert_recursively(current_node.right, value)

    def inorder_traversing(self, current_node = None): # We want to go through the tree and print the values - Revcursion is also a main component in this method
        
        # If we have a node, we check it
        if current_node is None:
            current_node = self.root

        if current_node is not None:
            # In this case I know that my node is not empty
            # We can use recursion here again to go through the tree
            if current_node.left is not None:
                self.inorder_traversing(current_node.left)
                print(current_node.value)
            if current_node.right is not None:
                self.inorder_traversing(current_node.right)
                print(current_node.value)



if __name__ == "__main__":
    binarytree = BinaryTree()

    testlist = [1, 3, 11, 55, 66, 4, 7]

    for i in testlist:
        binarytree.insert(i)

    binarytree.inorder_traversing()
