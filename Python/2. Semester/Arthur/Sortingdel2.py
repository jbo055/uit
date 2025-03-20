# Sorting og maxheap
import heapq

def shellsort(lst):
    n = len(lst)
    gap = n//2

    while gap > 0 :
        for current_index in range (gap, n):
            current_value = lst[current_index]
            previous_index = current_index
            while previous_index >= gap and lst[previous_index - gap] > current_value:
                # We shift the calue from left to right
                # We have to set the previous index

                lst[previous_index] = lst[previous_index - gap]
                previous_index -= gap

            lst[previous_index] = current_value

            

        gap //= 2
    return lst

class MaxHeap:
    def __init__(self, lst):
        self.heap = lst
        # We need a method to build the maxheap
        self.build_maxheap()
        # We need a method to insert elements to the max heap
        # We need to print the maxheap

    def build_maxheap(self):
        n = len(self.heap)
        for i in range(n):
            # Insert elements into the heap - heapify()
            self.heapify()


    def heapify(self, index):
        # Insert the element into the heap
        # The comparison between the elements is done here
        largest_index = index

        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        # In the if there has to be a comparison between the left and right child
        if left_child_index <  len(self.heap) and self.heap[left_child_index] > self.heap[largest_index]:
            largest_index = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest_index]:
            largest_index = right_child_index





    # def print_maxheap(self):

    def insert_into_maxheap(self):
        print("Inserting into the maxheap")


def main():
    # Shell sort O(n*log(n))
    # MAX HEAP which is the basis for HEAP SORT
    heap = MaxHeap()
    sorted = []

    while heap.heap:
        heap.build_maxheap()

        # We want to insert the items into the maxheap



    lst = [64, 34, 25, 12, 22, 11, 90]
    sortedlist = shellsort(lst.copy()) # Making sure that the original list is not changed


if __name__ == "__main__":
    main()