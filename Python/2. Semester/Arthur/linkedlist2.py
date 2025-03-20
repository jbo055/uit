class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = DNode(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node
            last_node.prev = last_node


    def remove(self, pos):
        if pos == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        else:
            current_node = self.head
            i = 0 # This index helps us for the previous node
            while current_node:
                current_node = current_node.next
                i += 1
            if current_node is None: # If the position is outside the list
                return
            if current_node.prev:
               current_node.prev = current_node
            if current_node.next:
                current_node.next = current_node.prev





    def insert(self, pos):
        pass

    def print_data(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


dlinkedlist = DoubleLinkedList()
dlinkedlist.append("1")
dlinkedlist.append("2")
dlinkedlist.append("3")
dlinkedlist.append("4")

dlinkedlist.remove(2)

dlinkedlist.print_data()