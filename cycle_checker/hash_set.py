class ListNode:
    """
    Definition for a singly linked list node.
    
    Attributes:
        val (int): Value of the node.
        next (ListNode): Reference to the next node in the linked list.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle_with_hashing(head):
    """
    Detects if the linked list has a cycle using a hash set to track visited nodes.
    
    Args:
        head (ListNode): The head of the linked list.

    Returns:
        bool: True if the linked list has a cycle, False otherwise.
    """
    visited = set()
    current = head

    while current:
        if current in visited:
            return True  # Cycle detected
        visited.add(current)
        current = current.next

    return False  # No cycle detected


# Example usage:
if __name__ == "__main__":
    # Create a linked list with a cycle
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Cycle created

    print("Has cycle (hashing):", has_cycle_with_hashing(node1))  # Output: True

    # Create a linked list without a cycle
    node5 = ListNode(1)
    node6 = ListNode(2)

    node5.next = node6

    print("Has cycle (hashing):", has_cycle_with_hashing(node5))  # Output: False
