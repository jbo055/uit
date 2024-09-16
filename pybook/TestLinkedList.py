from LinkedList import LinkedList

lst = LinkedList()

# Add elements to the list
lst.add("America") # Add America to the list
print("(1)", lst)

lst.insert(0, "Canada") # Add Canada to the beginning of the list
print("(2)", lst)

lst.add("Russia") # Add Russia to the end of the list
print("(3)", lst)

lst.addLast("France") # Add France to the end of the list
print("(4)", lst)

lst.insert(2, "Germany") # Add Germany to the list at index 2
print("(5)", lst)

lst.insert(5, "Norway") # Add Norway to the list at index 5
print("(6)", lst)

lst.insert(0, "Poland") # Same as list.addFirst("Poland")
print("(7)", lst)

# Remove elements from the list
lst.removeAt(0) # Remove the element at index 0
print("(8)", lst)

lst.removeAt(2) # Remove the element at index 2
print("(9)", lst)

lst.removeAt(lst.getSize() - 1) # Remove the last element
print("(10)", lst)
