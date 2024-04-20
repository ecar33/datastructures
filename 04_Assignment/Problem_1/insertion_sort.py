class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def insertion_sort(head):
    if not head:
        return head
    
    sorted_head = None  # Start with an empty sorted part
    
    # Process each node in the original list
    current = head
    while current:
        next_node = current.next  # Save the next node
        sorted_head = sorted_insert(sorted_head, current)  # Insert current in sorted order
        current = next_node  # Move to the next node
    
    return sorted_head

def sorted_insert(sorted_head, node):
    if not sorted_head or node.val < sorted_head.val:
        node.next = sorted_head
        return node
    
    # Find the correct insertion point
    current = sorted_head
    while current.next and current.next.val < node.val:
        current = current.next
    
    node.next = current.next
    current.next = node
    return sorted_head

def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

def main():
    # Create a linked list: 8 -> 2 -> 5 -> None
    list_node = ListNode(1)
    list_node.next = ListNode(3)
    list_node.next.next = ListNode(2)
    list_node.next.next.next = ListNode(0)

    print("Original List:")
    print_list(list_node)

    # Sort the list
    sorted_list = insertion_sort(list_node)

    print("Sorted List:")
    print_list(sorted_list)

if __name__ == "__main__":
    main()
