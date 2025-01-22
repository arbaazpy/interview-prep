def next_greater_element_brute_force(nums):
    """
    Finds the next greater element for each element in the array using a brute-force approach.
    
    Args:
        nums (list): List of integers.
        
    Returns:
        list: A list where each element is the next greater element of the corresponding index in the input array.
              If no greater element exists, the value is -1.
    """
    n = len(nums)
    result = [-1] * n
    
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                result[i] = nums[j]
                break
    
    return result


if __name__ == "__main__":
    nums = [4, 5, 2, 10, 8]
    print("Input Array:", nums)
    print("Next Greater Elements (Brute Force):", next_greater_element_brute_force(nums))
