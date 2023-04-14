#!/usr/bin/python3
"""Module minimum operation"""


def minOperations(n):
    """
    :param n: Calculates the minimum number of operations to go from one 'H' to n 'H's
    if the only available operations are "Copy All" and "Paste"
    :return: int with the number of operations
    """
    if n <= 1:
        return 0

    for i in range(2, int((n / 2) + 1)):
        if n % i == 0:
            return minOperations(int(n / i)) + i
    return n
