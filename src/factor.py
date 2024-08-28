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
    # To debug doctest test in pudb
    # Highlight the line of code below below
    # Type 't' to jump 'to' it
    # Type 's' to 'step' deeper
    # Type 'n' to 'next' over
    # Type 'f' or 'r' to finish/return a function call and go back to caller
    return "delete this and write your own code"


if __name__ == '__main__':
    # Execute doctests to protect main:
    import doctest

    doctest.testmod()

    # Run main:
    pass
    # YOUR CODE GOES HERE
