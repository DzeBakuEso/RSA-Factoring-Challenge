#!/usr/bin/python3

import sys


def factorize_number(n):
    # Simple function to find two factors of the number n
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return i, n // i
    return n, 1


def factorize_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                number = int(line.strip())
                p, q = factorize_number(number)
                print(f"{number}={p}*{q}")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except ValueError:
        print("Invalid number in the file.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
    else:
        factorize_file(sys.argv[1])
