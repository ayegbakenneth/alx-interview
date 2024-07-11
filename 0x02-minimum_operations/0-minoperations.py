#!/usr/bin/env python3
""" File executable path """


def minOperations(n):
    """ Function performing mininum operation """
    if n <= 1:
        return 0
    task = 0
    done_task = 2
    while n > 1:
        while n % done_task == 0:
            task += done_task
            n /= done_task
        done_task += 1
    return task
