class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def search(self, e):
        return self.searchHelper(self.root, e) # Start from the root

    def searchHelper(self, current, e): # Search from the current subtree
        if current == None:
            return False
        elif e < current.element:
            return self.searchHelper(current.left, e)
        elif e == current.element:
            return True
        else:
            return self.searchHelper(current.right, e)
    
    # Insert element e into the binary search tree
    # Return True if the element is inserted successfully 
    def insert(self, e):
        if self.root == None:
            self.root = self.createNewNode(e) # Create a new root
        else:
            # Locate the parent node
            parent = None
            current = self.root
            while current != None:
                if e < current.element:
                    parent = current
                    current = current.left
                elif e > current.element:
                    parent = current
                    current = current.right
                else:
                    return False # Duplicate node not inserted

            # Create the new node and attach it to the parent node
            if e < parent.element:
                parent.left = self.createNewNode(e)
            else:
                parent.right = self.createNewNode(e)

        self.size += 1 # Increase tree size
        return True # Element inserted

    # Create a new TreeNode for element e
    def createNewNode(self, e):
        return TreeNode(e)

    # Return the size of the tree
    def getSize(self):
        return self.size
    
    # Inorder traversal from the root
    def inorder(self):
        self.inorderHelper(self.root)

    # Inorder traversal from a subtree 
    def inorderHelper(self, r):
        if r != None:
            self.inorderHelper(r.left)
            print(r.element, end = " ")
            self.inorderHelper(r.right)

    # Postorder traversal from the root 
    def postorder(self):
        self.postorderHelper(self.root)

    # Postorder traversal from a subtree 
    def postorderHelper(self, root):
        if root != None:
            self.postorderHelper(root.left)
            self.postorderHelper(root.right)
            print(root.element, end = " ")

    # Preorder traversal from the root 
    def preorder(self):
        self.preorderHelper(self.root)

    # Preorder traversal from a subtree 
    def preorderHelper(self, root):
        if root != None:
            print(root.element, end = " ")
            self.preorderHelper(root.left)
            self.preorderHelper(root.right)

    # Returns a path from the root leading to the specified element 
    def path(self, e):
        list = []
        current = self.root # Start from the root

        while current != None:
            list.append(current) # Add the node to the list
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else:
                break

        return list # Return an array of nodes

    # Delete an element from the binary search tree.
    # Return True if the element is deleted successfully
    # Return False if the element is not in the tree 
    def delete(self, e):
        # Locate the node to be deleted and its parent node
        parent = None
        current = self.root
        while current != None:
            if e < current.element:
                parent = current
                current = current.left
            elif e > current.element: 
                parent = current
                current = current.right
            else:
                break # Element is in the tree pointed by current

        if current == None:
            return False # Element is not in the tree

        # Case 1: current has no left children
        if current.left == None:
            # Connect the parent with the right child of the current node
            if parent == None:
                self.root = current.right
            else:
                if e < parent.element:
                    parent.left = current.right
                else:
                    parent.right = current.right
        else:
            # Case 2: The current node has a left child
            # Locate the rightmost node in the left subtree of
            # the current node and also its parent
            parentOfRightMost = current
            rightMost = current.left

            while rightMost.right != None:
                parentOfRightMost = rightMost
                rightMost = rightMost.right # Keep going to the right

            # Replace the element in current by the element in rightMost
            current.element = rightMost.element

            # Eliminate rightmost node
            if parentOfRightMost.right == rightMost:
                parentOfRightMost.right = rightMost.left
            else:
                # Special case: parentOfRightMost == current
                parentOfRightMost.left = rightMost.left     

        self.size -= 1
        return True # Element deleted

    # Return true if the tree is empty
    def isEmpty(self):
        return self.size == 0
        
    # Remove all elements from the tree
    def clear(self):
        self.root == None
        self.size == 0

    # Return the root of the tree
    def getRoot(self):
        return self.root

class TreeNode:
    def __init__(self, e):
        self.element = e
        self.left = None  # Point to the left node, default None
        self.right = None # Point to the right node, default None

class MyBST(BST):
    def __init__(self):
        BST.__init__(self)
        
    # Return an iterator for a BST
    def __iter__(self):
        return BSTIterator(self.root)

class BSTIterator: # in- order iterator for BST
    # Write code for BSTIterator here
    def __init__(self, root):
        self.stack = [] # Stack to store the nodes
        self.current = root # Current node
        self._pushLeft(root)

    def _pushLeft(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left

    def __iter__(self):
        return self
    
    def __next__(self):
        if len(self.stack) == 0:
            raise StopIteration
        node = self.stack.pop()
        self._pushLeft(node.right)
        return node.element
    
    def __len__(self):
        return len(self.stack)
    
    def __str__(self):
        return " ".join(str(node.element) for node in self.stack)
    


def main():
    tree = MyBST()

    s = input("Enter integers in one line for tree separated by space: ");
    list1 = [int(x) for x in s.split()]
    for e in list1:
        tree.insert(e)
       
    print(s, "are inserted into the tree")
    print("In-order traverse should give sorted order: ", end = '')
   
    iterator = iter(tree) # Create an iterator
    try:
        while True:
            print(next(iterator), end = ' ')
    except StopIteration:
        print("All traversed")
    print("Max element:", max(tree)) # Print the max element in the tree
    print("Min element:", min(tree)) # Print the min element in the tree
    print("Sum:",sum(tree)) # Print the sum of all elements in the tree
    print("Set:", set(tree)) # Print the set
    print("List:", list(tree)) # Print the list
   

    
main()