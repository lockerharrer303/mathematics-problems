def is_palindrome(s: str) -> bool:
    """
    Check if the given string s is a palindrome.
    
    A palindrome is a word, phrase, or sequence that reads the same backward as forward.
    
    Args:
        s (str): The input string to check for being a palindrome.
        
    Returns:
        bool: True if the input string is a palindrome, False otherwise.
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_s = ''.join(c.lower() for c in s if c.isalnum())
    
    return cleaned_s == cleaned_s[::-1]

# Example usage
print(is_palindrome("A man, a plan, a canal, Panama!"))  # True
print(is_palindrome("Hello, World!"))  # False
