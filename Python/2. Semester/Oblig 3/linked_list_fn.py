# Filename: linked_list_fn.py
# Følgende metoder er "left as an exercise" i LinkedList-klassen:
# clear, contains, remove, get, indexOf, lastIndexOf, set
class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    # Return the head element in the list 
    def get_first(self):
        if self._size == 0:
            return None
        else:
            return self._head.element
    
    # Return the last element in the list 
    def get_last(self):
        if self._size == 0:
            return None
        else:
            return self._tail.element

    # Add an element to the beginning of the list 
    def add_first(self, e):
        new_node = Node(e)  # Create a new node
        new_node.next = self._head  # link to "what was first"
        self._head = new_node  # head points to the new node
        self._size += 1  # Increase list size

        if self._tail is None:  # the new node is the only node in list
            self._tail = self._head

    # Add an element to the end of the list 
    def add_last(self, e):
        new_node = Node(e)  # Create a new node for e
    
        if self._tail is None:
            self._head = self._tail = new_node  # The only node in list
        else:
            self._tail.next = new_node  # Link the new with the last node
            self._tail = self._tail.next  # tail now points to the last node
    
        self._size += 1  # Increase size

    # Same as add_last 
    def add(self, e):
        self.add_last(e)

    # Insert a new element at the specified index in this list
    # The index of the head element is 0 
    def insert(self, index, e):
        if index == 0:
            self.add_first(e)  # Insert first
        elif index >= self._size:
            self.add_last(e)  # Insert last
        else:  # Insert in the middle
            current = self._head
            for i in range(1, index):
                current = current.next
            temp = current.next
            current.next = Node(e)
            current.next.next = temp
            self._size += 1

    # Remove the head node and
    #  return the object that is contained in the removed node. 
    def remove_first(self):
        if self._size == 0:
            return None  # Nothing to delete
        else:
            temp = self._head  # Keep the first node temporarily
            self._head = self._head.next  # Move head to point the next node
            self._size -= 1  # Reduce size by 1
            if self._head is None: 
                self._tail = None  # List becomes empty 
            return temp.element  # Return the deleted element

    # Remove the last node and
    # return the object that is contained in the removed node
    def remove_last(self):
        if self._size == 0:
            return None  # Nothing to remove
        elif self._size == 1:  # Only one element in the list
            temp = self._head
            self._head = self._tail = None  # list becomes empty
            self._size = 0
            return temp.element
        else:
            current = self._head
        
            for i in range(self._size - 2):
                current = current.next
        
            temp = self._tail
            self._tail = current
            self._tail.next = None
            self._size -= 1
            return temp.element

    # Remove the element at the specified position in this list.
    #  Return the element that was removed from the list. 
    def remove_at(self, index):
        if index < 0 or index >= self._size:
            return None  # Out of range
        elif index == 0:
            return self.remove_first()  # Remove first 
        elif index == self._size - 1:
            return self.remove_last()  # Remove last
        else:
            previous = self._head
    
            for i in range(1, index):
                previous = previous.next
        
            current = previous.next
            previous.next = current.next
            self._size -= 1
            return current.element

    # Return true if the list is empty
    def is_empty(self):
        return self._size == 0
    
    # Return the size of the list
    def get_size(self):
        return self._size

    def __str__(self):
        result = "["

        current = self._head
        for i in range(self._size):
            result += str(current.element)
            current = current.next
            if current is not None:
                result += ", "  # Separate two elements with a comma
            else:
                result += "]"  # Insert the closing ] in the string

        return result

    # Clear the list
    def clear(self):
        self._head = self._tail = None
        self._size = 0

    # Return true if this list contains the element e 
    def contains(self, e):
        current = self._head
        while current:
            if current.element == e:
                return True
            current = current.next
        return False


    # Remove the element and return true if the element is in the list 
    def remove(self, e):
        current = self._head
        previous = None
        while current:
            if current.element == e:
                if previous:
                    previous.next = current.next # Hopper over hvis e
                else:
                    self._head = current.next
                if current == self._tail:
                    self._tail = previous
                self._size -= 1
                return True
            previous = current
            current = current.next
        return False

    # Return the element from this list at the specified index 
    def get(self, index):
        if index < 0 or index >= self._size: # Check if index is in range
            return None
        current = self._head
        for i in range(index):
            current = current.next
        return current.element

    # Return the index of the head matching element in this list.
    # Return -1 if no match.
    def index_of(self, e):
        current = self._head
        index = 0
        while current:
            if current.element == e:
                return index
            index += 1
            current = current.next

        return -1

    # Return the index of the last matching element in this list
    #  Return -1 if no match. 
    def last_index_of(self, e):
        current = self._head
        index = -1
        current_index = 0
        while current:
            if current.element == e:
                index = current_index
            current = current.next
            current_index += 1
        return index
                

    # Replace the element at the specified position in this list
    #  with the specified element.
    def set(self, index, e):
        if index < 0 or index >= self._size: # Check if index is in range
            return None
        current = self._head
        for i in range(index):
            current = current.next # Move to the specified index
        current.element = e # Replace element when index is found
            
    
    # Return elements via indexer, can use list[0] to get the first element etc
    def __getitem__(self, index):
        return self.get(index)

    # Return an iterator for a linked list
    def __iter__(self):
        return LinkedListIterator(self._head)
    
# The Node class
class Node:
    def __init__(self, e):
        self.element = e
        self.next = None

class LinkedListIterator: 
    def __init__(self, head):
        self._current = head
        
    def __next__(self):
        if self._current is None:
            raise StopIteration
        else:
            element = self._current.element
            self._current = self._current.next
            return element