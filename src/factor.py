#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


def factor(num: int) -> list[int]:
    """
    Purpose:        Factors positive integers
    Parameters:     A decimal number, as an integer
    User Input:     No
    Prints:         Nothing
    Returns:        Result as a list of int
    Modifies:       Nothing
    Calls:          Basic python only
    Tests:          ./unit_tests/*
    Status:         Done!

    Usage illustrated via some simple doctests:
    >>> factor(8)
    [1, 2, 4, 8]

    >>> factor(10)
    [1, 2, 5, 10]

    >>> import random
    >>> for _ in range(5):
    ...     num = random.randint(0, 200)
    ...     assert factor(num) == [i for i in range(1, num // 2 + 1) if not num % i] + [num]

    >>> for _ in range(2):
    ...     num = random.randint(0, 200)
    ...     factor(num) == [i for i in range(1, num // 2 + 1) if not num % i] + [num]
    True
    True

    >>> print("Unlike other frameworks, doctest does stdout easily")
    Unlike other frameworks, doctest does stdout easily
    """
    return [i for i in range(1, num + 1) if num % i == 0]


def main() -> None:
    # Main driver function
    if len(sys.argv) == 3:
        # Argument-based input: reading integer from input file and writing to output file
        try:
            # Read the integer from the input file
            with open(sys.argv[1], "r") as input_file:
                num = int(input_file.read().strip())

            # Write the factors to the output file
            with open(sys.argv[2], "w") as output_file:
                factors = factor(num)
                output_file.write(str(factors))

            print(f"Factors of {num} written to {sys.argv[2]}")
        except ValueError:
            print("Please provide a valid integer in the input file.")
        except FileNotFoundError:
            print("Input or output file not found.")
    else:
        # Standard input/output
        try:
            num = int(input("Enter an integer to factor: "))
            print(f"Factors of {num}: {factor(num)}")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


if __name__ == "__main__":
    # Execute doctests to protect main:
    import doctest

    doctest.testmod()

    # Run main:
    main()
