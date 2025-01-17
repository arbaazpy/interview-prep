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


def has_cycle(head):
    """
    Detects if the linked list has a cycle.
    
    This function uses Floyd's Cycle Detection Algorithm, which employs two pointers 
    (slow and fast). If a cycle exists, the two pointers will eventually meet; otherwise, 
    the fast pointer will reach the end of the list.

    Args:
        head (ListNode): The head of the linked list.

    Returns:
        bool: True if the linked list has a cycle, False otherwise.
    """
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next         # Move slow pointer one step
        fast = fast.next.next    # Move fast pointer two steps

        if slow is fast:
            return True  # Cycle detected

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
    node4.next = node2  # Cycle created by pointing back to node2

    print("Has cycle:", has_cycle(node1))  # Output: True

    # Create a linked list without a cycle
    node5 = ListNode(1)
    node6 = ListNode(2)

    node5.next = node6

    print("Has cycle:", has_cycle(node5))  # Output: False
