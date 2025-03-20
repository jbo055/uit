# Manuell implementasjon av HeapSort
def heapify(arr, n, i):
    largest = i # Initielt er roten størst
    left = 2 * i + 1 # Venstre barn
    right = 2 * i + 2 # Høyre barn

    # Sjell om venstre barn finner og er større enn roten
    if left < n and arr[i] < arr[left]:
        largest = left

    # Sjekk om høyre barn finnes og er større enn roten
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Hvis en største ikke er roten, bytt og heapify videre
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    # Bygg heapen (omarranger arrayet)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Ett for ett, trekk ut elementene fra heapen
    for i in range(n - 1, 0, -1):
        #Flytt nåværende rot til slutten
        arr[0], arr[i] = arr[i], arr[0]
        # Kall heapify på den reduserte heapen
        heapify(arr, i, 0)

# Eksempelbruk
# if __name__ == "__main__":
#     data = [12, 11, 13, 5, 6, 7]
#     print("Opprinnelig array:", data)
#     heapSort(data)
#     print("Sortert array:", data)


# Med bruk av heapq-modulen
import heapq

def heapsort_heapq(iterable):
    # Inverter elementene for å få max-heap-effekt
    h = [-x for x in iterable]
    heapq.heapify(h)
    return [-heapq.heappop(h) for i in range(len(h))]

# Eksempelbruk
if __name__ == "__main__":
    data = [12, 11, 13, 5, 6, 7]
    print("Opprinnelig array:", data)
    data = heapsort_heapq(data)
    print("Sortert array:", data)


