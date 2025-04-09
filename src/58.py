def is_palindrome(s):
    """
    Check if the given string s is a palindrome.
    
    A palindrome is a word, phrase, or sequence that reads the same backward as forward.
    For example, "madam" and "racecar" are palindromes.
    
    Parameters:
    s (str): The string to check.
    
    Returns:
    bool: True if s is a palindrome, False otherwise.
    """
    return s.lower() == s.lower()[::-1]

# Example usage
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("Hello, World!"))  # False
