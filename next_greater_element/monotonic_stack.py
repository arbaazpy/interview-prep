def next_greater_element_stack(nums):
    """
    Finds the next greater element for each element in the array using a stack.
    
    Args:
        nums (list): List of integers.
        
    Returns:
        list: A list where each element is the next greater element of the corresponding index in the input array.
              If no greater element exists, the value is -1.
    """
    n = len(nums)
    result = [-1] * n
    stack = []
    
    for i in range(n):
        # While stack is not empty and the current element is greater than the top of the stack
        while stack and nums[i] > nums[stack[-1]]:
            index = stack.pop()
            result[index] = nums[i]
        stack.append(i)  # Push current index onto the stack

    return result


if __name__ == "__main__":
    nums = [4, 5, 2, 10, 8]
    print("Input Array:", nums)
    print("Next Greater Elements (Stack):", next_greater_element_stack(nums)) # [5, 10, 10, -1, -1]
    print()
    nums = [1, 4, 6, 3, 2, 7]
    print("Input Array:", nums)
    print("Next Greater Elements (Stack):", next_greater_element_stack(nums)) # [4, 6, 7, 7, 7, -1]
