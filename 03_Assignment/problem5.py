class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        max_val = self.heap.pop()
        self._heapify_down(0)
        return max_val

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        # Check if left child exists and is greater than root
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        # Check if right child exists and is greater than root
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        # Change root if needed
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            # Heapify the root
            self._heapify_down(largest)

    def get_max(self):
        return self.heap[0] if self.heap else None

max_heap = MaxHeap()
nums = [3, 10, 1000, -99, 4, 100]
for num in nums:
    max_heap.insert(num)

k = 3
result = []

for i in range(k): 
  result.append(max_heap.extract_max())
  
print(f'Input: {nums} and k = {k}')
print(f'Output: {result}')