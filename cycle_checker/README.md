# Detect Cycle in a Linked List

This project demonstrates two approaches to detect if a **linked list** has a cycle:

1. **Hashing Approach**: Uses a hash set to keep track of visited nodes.
2. **Floyd's Cycle Detection Algorithm**: Utilizes two pointers (slow and fast) to detect cycles efficiently.

## Problem Statement

A **cycle** in a linked list occurs when a node's `next` pointer references a previous node in the list, forming a loop. The task is to determine whether a given singly linked list contains a cycle.

---

## Approach 1: Hashing Approach

### Description:
This approach uses a hash set to track the nodes that have already been visited. If a node is visited twice, a cycle exists.

### Code:

```python
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
```

### Time Complexity:
* **Time Complexity:** O(N), where `N` is the number of nodes in the linked list. Each node is visited once.
* **Space Complexity:** O(N), as a hash set is used to store visited nodes.

---

## Approach 2: Floyd's Cycle Detection Algorithm

### Description:
This algorithm uses two pointers:
- A **slow pointer** that moves one step at a time.
- A **fast pointer** that moves two steps at a time.

If there is a cycle, the two pointers will eventually meet. Otherwise, the fast pointer will reach the end of the list.

### Code:

```python
def has_cycle(head):
    """
    Detects if the linked list has a cycle using Floyd's Cycle Detection Algorithm.
    
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
```

### Time Complexity:
* **Time Complexity:** O(N), where `N` is the number of nodes in the linked list.
* **Space Complexity:** O(1), as it uses only two pointers.

---

### When to Use Which Approach

| **Approach**       | **Time Complexity** | **Space Complexity** | **Notes**                                     |
|---------------------|---------------------|-----------------------|-----------------------------------------------|
| **Hashing**         | O(N)               | O(N)                  | Simple to implement but requires extra space. |
| **Floyd's Algorithm** | O(N)               | O(1)                  | Most efficient, uses no extra space.          |

---

### Example Usage

#### Input 1: Linked List with a Cycle
- **Nodes**: `3 → 2 → 0 → -4 → (cycle back to 2)`
- **Output**: `True`

#### Input 2: Linked List without a Cycle
- **Nodes**: `1 → 2 → None`
- **Output**: `False`

---

### Conclusion

1. **Hashing Approach**: A simple method, but requires additional memory for a hash set.
2. **Floyd's Cycle Detection Algorithm**: The most efficient method with constant space and linear time complexity.
