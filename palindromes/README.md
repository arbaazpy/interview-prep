# Palindrome Checker

This project demonstrates two different approaches for checking whether a given string is a **palindrome**:

1. **Lambda Function Approach**: A concise, one-liner lambda function that checks if a string is a palindrome by comparing it with its reverse.
2. **Two-Pointer Technique**: An efficient approach using two pointers to compare characters from both ends of the string.

## Problem Statement

A **palindrome** is a word, phrase, or sequence that reads the same backward as forward. The task is to determine whether each string in a given list is a palindrome.

---

## Approach 1: Lambda Function Approach

### Description:
This approach uses a Python lambda function to check if a string is a palindrome by comparing the string with its reversed version.

### Code:

```python
# Lambda function to check if a string is a palindrome
is_palindrome = lambda s: s == s[::-1]

def check_palindromes(inputs):
    """
    Function to check and print whether each string in the provided list is a palindrome.
    
    Args:
        inputs (list of str): List of strings to check for palindromes.
    """
    for word in inputs:
        # Check if the current word is a palindrome
        if is_palindrome(word):
            print(f"'{word}' is a palindrome")
        else:
            print(f"'{word}' is not a palindrome")

if __name__ == "__main__":
    # List of words to check for palindromes
    inputs = ["civic", "rotor", "madam", "deified", "reviver", "humor"]
    
    # Call the function to check the words
    check_palindromes(inputs)
```

### Time Complexity:
* **Time Complexity:** O(N) per string, where `N` is the length of the string.
* **Space Complexity:** O(1), as it only uses a constant amount of additional space.

---

## Approach 2: Two-Pointer Technique

### Description:
This approach uses two pointers: one starting at the beginning and the other at the end of the string. The characters at these pointers are compared, and the pointers move towards the center until they meet.

### Code:

```python
# Function to check if a string is a palindrome using the two-pointer technique
def is_palindrome(string):
    """
    Check if a string is a palindrome.

    Args:
        string (str): The string to be checked.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    left = 0
    right = len(string) - 1
    
    # Compare characters from both ends towards the center
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
        
    return True

def check_palindromes(inputs):
    """
    Function to check and print whether each string in the provided list is a palindrome.
    
    Args:
        inputs (list of str): List of strings to check for palindromes.
    """
    for word in inputs:
        # Check if the current word is a palindrome
        if is_palindrome(word):
            print(f"'{word}' is a palindrome")
        else:
            print(f"'{word}' is not a palindrome")

if __name__ == "__main__":
    # List of words to check for palindromes
    inputs = ["civic", "rotor", "madam", "deified", "reviver", "humor"]
    
    # Call the function to check the words
    check_palindromes(inputs)
```

### Time Complexity:
* **Time Complexity:** O(N) per string, where `N` is the length of the string.
* **Space Complexity:** O(1), as it only uses a constant amount of additional space.

---

### When to Use Which Approach

* **Lambda Function Approach:**
  * Use this approach when you want a simple, concise solution.
  * Ideal for quick, small-scale palindrome checks.

* **Two-Pointer Technique:**
  * Use this approach when you need a more efficient and clear algorithm.
  * Suitable for larger strings and cases where performance is crucial.

---

### Conclusion
* **Lambda Function Approach:** A quick and easy method to check palindromes.
* **Two-Pointer Technique:** A more explicit and efficient algorithm for palindrome checking.
---

