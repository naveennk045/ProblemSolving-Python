import re

def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    # Check if the cleaned string is equal to its reverse
    print(cleaned)
    return cleaned == cleaned[::-1]

# Test cases
print(is_palindrome("A man, a plan, a canal, Panama"))  # Output: True
print(is_palindrome("hello"))  # Output: False
