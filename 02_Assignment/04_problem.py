class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
      
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __bool__(self):
      return self.head is not None and self.tail is not None

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
    
def level_order_traversal(root):
  q = Queue()
  q.enqueue(root)
  result = []
  while q:
    current_node = q.dequeue()
    result.append(str(current_node.val) + ' ')
    if current_node.left != None:
      q.enqueue(current_node.left)
    if current_node.right != None:
      q.enqueue(current_node.right)
  return result
  


if __name__ == "__main__":
  root = TreeNode(1)
  root.right = TreeNode(2)
  root.right.left = TreeNode(3)

  traversal_result = level_order_traversal(root)

  print(f'Output: {traversal_result}')
