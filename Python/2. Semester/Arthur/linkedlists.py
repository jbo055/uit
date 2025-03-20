class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data) # Creating an object in a class can be very problematic for performance
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def printlist(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove_item(self):
        pass

def main():
    linkedlist = LinkedList() # We create an object for LinkedList
    linkedlist.append("1")
    linkedlist.append("2")
    linkedlist.append("3")

    linkedlist.printlist()

if __name__ == "__main__":
    main()