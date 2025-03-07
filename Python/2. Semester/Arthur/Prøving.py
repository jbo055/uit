list = [90, 34, 25, 12, 22, 11, 64] # Global list which we will use for the whole example

def compare(a, b):
    return a > b # It returns True if a is greater than b, otherwise it returns False

def swap(list, i, j):
    list[i], list[j] = list[j], list[i] # Swaps the elements in the list

def bubblesort(list):
    n = len(list) # Length of the list

    for i in range(n): # 0, 1, 2, 3, 4, ...
        for j in range(0, n-i-1): # Length of the list minus place in the list minus 1
            if compare(list[j], list[j+1]): # If the element in the list is greater than the next element in the list
                swap(list, j, j+1) # Swap the elements in the list
                print(list, i, j)
# Advantage: Easy to implement, easy to understand, it is possible to implement it everywhere(every programming language)
# Disadvantage: All the comparissons are made anyway, so completely unneccessary comparissons are made
# Complexity: O(n^2)
# Stability: Inplace - I do not need extra memory to sort the list - Stable

# bubblesort(list) # Call the bubblesort function with the list as an argument
# print("Sorted array is:", list) # Print the sorted list

def findsmallestvalue(list, start):
    smallest_index = start
    for i in range(start+1, len(list)):
        if list[i] < list[smallest_index]:
            smallest_index = i
    return smallest_index

def selectionsort(list):
    # Find smallest element in the list
    # Iterate through the list and swap (we use indexes to swap the elements)
    n = len(list)
    for i in range(n):
        smallest_index = findsmallestvalue(list, i)
        swap(list, i, smallest_index)
        print(list, i, smallest_index)
# Advantage: Easy to implement, easy to understand, it is possible to implement it everywhere(every programming language)
# Disadvantage: All the comparissons are made anyway, so completely unneccessary comparissons are made
# Complexity: O(n^2)
# Stability: Inplace - I do not need extra memory to sort
# Selectionsort is faster than bubblesort, because it does not make as many comparissons as bubblesort
# Bubblesort is stable, but selectionsort is not stable

# selectionsort(list)
# print("Sorted array is:", list)
        

def insertionsort(list):
    n = len(list)
    for i in range(1, n):
        key = list[i]
        j = i - 1 # Previous index of previous element
        # Right shifts the elements in the list - We want to shift the bigger values to the right
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key # Insert the key in the right place
        print(list, i, j)

insertionsort(list)
print("Sorted array is:", list)



