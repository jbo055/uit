def quicksort(arr):
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