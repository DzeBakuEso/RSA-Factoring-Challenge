#!/usr/bin/python3

import sys
import math


def is_prime(n):
    """Check if a number is prime."""
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


def factorize_rsa_number(n):
    """Factorize the number and return two prime factors if they exist."""
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            p, q = i, n // i
            if is_prime(p) and is_prime(q):
                return p, q
    return None, None


def factorize_file(filename):
    """Read file, factorize the RSA number, and ensure the factors are prime."""
    try:
        with open(filename, 'r') as file:
            for line in file:
                number = int(line.strip())
                p, q = factorize_rsa_number(number)
                if p and q:
                    print(f"{number}={p}*{q}")
                else:
                    print(f"Could not factorize {number} into two prime numbers.")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except ValueError:
        print("Invalid number in the file.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: rsa <file>")
    else:
        factorize_file(sys.argv[1])
