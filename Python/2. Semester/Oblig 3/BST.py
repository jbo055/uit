class TreeNode:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None
        self._parent = None  

    def insert(self, element):
        if element < self.element:
            if self.left is None:
                self.left = TreeNode(element)
                self.left._parent = self

                print(f"{element} are inserted into tree")

            else:
                self.left.insert(element)

        elif element > self.element:
            
            if self.right is None:
                self.right = TreeNode(element)
                self.right._parent = self

                print(f"{element} are inserted into tree")

            else:
                self.right.insert(element)

        else:
            # elementet finnes allerede, gjør ingenting eller håndter duplikater her
            pass

    def getNode(self, element):
        if self.element == element:
            return self
        
        elif element < self.element and self.left is not None:
            return self.left.getNode(element)
        
        elif element > self.element and self.right is not None:
            return self.right.getNode(element)
        
        else:
            return None

    def isLeaf(self, element):
        node = self.getNode(element)

        if node is None:
            return False
        
        return node.left is None and node.right is None

    def getPath(self, e):
        node = self.getNode(e)
        path = []

        while node is not None:
            path.append(node.element)
            node = node._parent

        return path

    def delete(self, element):
        if element < self.element:

            if self.left is not None:
                self.left = self.left.delete(element)

                if self.left is not None:
                    self.left._parent = self

            return self
        
        elif element > self.element:

            if self.right is not None:
                self.right = self.right.delete(element)

                if self.right is not None:
                    self.right._parent = self

            return self
        
        else:
            # funnet noden som skal slettes
            if self.left is None and self.right is None:
                return None  # slett bladnode
            
            if self.left is None:
                child = self.right
                child._parent = self._parent
                return child
            
            elif self.right is None:
                child = self.left
                child._parent = self._parent
                return child
            
            else:
                pred = self.left

                while pred.right is not None:
                    pred = pred.right

                self.element = pred.element  # kopier verdien
                self.left = self.left.delete(pred.element)

                if self.left is not None:
                    self.left._parent = self

                return self


# Hovedprogrammet
if __name__ == "__main__":
    # Leser inn tall fra bruker og bygger treet
    tall_str = input("Enter integers in one line for tree separated by space: ")
    tall_liste = list(map(int, tall_str.split()))
    if not tall_liste:
        exit()

    # Første element blir rotnoden
    rot = TreeNode(tall_liste[0])
    print(f"{tall_liste[0]} are inserted into tree")
    for t in tall_liste[1:]:
        rot.insert(t)

    # Slett noden med element 50
    print("Deletes 50")
    rot = rot.delete(50)
    
    # Eksempel: sjekk for nodene med verdiene 90 og 5
    if rot.getNode(90) and rot.isLeaf(90):
        print(f"90 is a leaf, values to root is {rot.getPath(90)}")
    if rot.getNode(5) and rot.isLeaf(5):
        print(f"5 is a leaf, values to root is {rot.getPath(5)}")
