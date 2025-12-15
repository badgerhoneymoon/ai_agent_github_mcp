"""
Palindrome detector.

This module provides a single function:
- is_palindrome(s) -> bool
"""


def is_palindrome(s: str) -> bool:
    """
    Check if the given string is a palindrome (case-sensitive, exact characters).

    Args:
        s: Input string.

    Returns:
        True if s reads the same forwards and backwards, False otherwise.
    """
    return s == s[::-1]


if __name__ == "__main__":
    examples = ["racecar", "level", "hello", "abba"]
    for e in examples:
        print(f"{e}: {is_palindrome(e)}")
