# Lag en klasse UniqueQueue som oppfører seg som en kø, 
# men som ikke kan inneholde duplikater.
# Du skal kunne iterere over køen, så du må 
# lage en iterator.



class Data:
    def __init__(self, root):
        self.root = root
        self.next = None
        self.prev = None

class UniqueQueue:
    def __init__(self):
        self.head = None

    def append(self, root):
        new_node = UniqueQueue(root)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node
            last_node.prev = last_node

    def __iter__(self):
        return UQIterator(self.root)


class UQIterator:
    def __init__(self, root):
        self.stack = [] 
        self.current = root 
        
    

        
        
# queue = UniqueQueue()
#     queue.enqueue(1)
#     queue.enqueue(2)
#     queue.enqueue(3)
#     queue.enqueue(2)  # Duplicate, will not be added
#     queue.enqueue(4)

#     print("Queue contents:")
#     for item in queue:
#         print(item)

#     print("\nDequeueing items:")
#     while len(queue) > 0:
#         print(queue.dequeue())

#     print("\nQueue is now empty.")