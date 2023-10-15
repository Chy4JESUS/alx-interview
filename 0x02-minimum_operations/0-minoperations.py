#!/usr/bin/python3
"""
File:
0x02-minimum_operations/0-minoperations.py
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    """
    given = "H"
    cp_ch = ""

    given_len = 1
    operation = 0

    while given_len < n:
        if n % given_len == 0:
            cp_ch = given
            operation += 1
        given += cp_ch
        given_len = len(given)
        operation += 1
    return operation
