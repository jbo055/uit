

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Mergesort for the first half
        mergesort(left_half)

        # Mergesort for the second half
        mergesort(right_half)

        i = 0
        j = 0
        k = 0
        
        # Here the sorting is done
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1

            else:
                arr[k] = right_half[j]
                j += 1

            k += 1

        # Here we add the sorted values to the existing list
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr


def quicksort(arr):
    # Need to set a pivot element to compare the other elements to
    if len(arr) <= 1:
        return arr
    
    first = arr[0]
    mid = arr[len(arr) // 2]
    last = arr[-1]
    pivot = sorted([first, mid, last])[1]

    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    return quicksort(less) + equal + quicksort(greater)

arr = [38, 22, 25, 43, 9, 82]
print(quicksort(arr))
# Quicksort
print(mergesort(arr))
# Mergesort
