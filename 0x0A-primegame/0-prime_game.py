#!/usr/bin/python3
"""The file executable path"""


def isWinner(x, nums):
    """A function that decides a winner"""
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None
    prime = 0
    also_prime = 0
    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for i in range(2, len(a)):
        rm_multiples(a, i)
    """ Start the game """
    for i in nums:
        """ prime wins if set of numbers are even """
        if sum(a[0:i + 1]) % 2 == 0:
            prime += 1
        else:
            also_prime += 1
    """ This decides the winner of the game """
    if prime > also_prime:
        return "Ben"
    if also_prime > prime:
        return "Maria"
    return None


def rm_multiples(ls, x):
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
