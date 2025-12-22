#!/usr/bin/env python3

"""prime_checker.py
Simple program to list prime numbers between 1 and 50.
"""

def is_prime(n):
    """Return True if n is prime, False otherwise."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def main():
    primes = [n for n in range(1, 51) if is_prime(n)]
    print("Prime numbers between 1 and 50:")
    print(", ".join(map(str, primes)))


if __name__ == '__main__':
    main()
