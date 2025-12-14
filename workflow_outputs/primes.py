def is_prime(n: int) -> bool:
    """Return True if n is a prime number, otherwise False.

    - Primes are integers greater than 1 that have no positive divisors other than 1 and themselves.
    - Returns False for non-integer inputs as well as n <= 1.
    """
    # Validate input type
    if not isinstance(n, int):
        return False
    if n <= 1:
        return False
    if n == 2:
        return True 
    # Check divisors from 2 up to sqrt(n)
    limit = int(n ** 0.5)
    for i in range(2, limit + 1):
        if n % i == 0:
            return False
    return True
