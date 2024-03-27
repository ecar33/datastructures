def min_heapify(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] < arr[smallest]:
        smallest = left
    
    if right < n and arr[right] < arr[smallest]:
        smallest = right
    
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, n, smallest)

def build_min_heap(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        min_heapify(arr, n, i)
    return arr

# Given numbers
numbers = [8, 12, 9, 7, 22, 3, 26, 14, 11, 15, 22]
min_heap = build_min_heap(numbers)
print(min_heap)