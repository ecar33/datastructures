class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, arg):
        new_node = Node(arg)
        if self.tail is None:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
      if self.head is None:  # Check if the queue is empty
        return None  # Or raise an exception, e.g., raise IndexError("dequeue from empty queue")
      
      to_delete = self.head
      self.head = self.head.next
      
      if self.head is None:
        self.tail = None
      return to_delete.data

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next

        return " -> ".join(elements)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.enqueue(4)
q.dequeue()
print(q)
