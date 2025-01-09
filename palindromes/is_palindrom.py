# Lambda function to check if a string is a palindrome
# A palindrome is a word that reads the same backward as forward
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
