def is_palindrome(s: str) -> bool:
    """Return True if the given string s is a palindrome (case-sensitive, no normalization)."""
    return s == s[::-1]
