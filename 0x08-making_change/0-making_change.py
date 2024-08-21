#!/usr/bin/env python3
""" File executable path """


def makeChange(coins, total):
    """ Function that uses different coins
    based on their value to reach a near total """
    if sum_total <= 0:
        return 0
    see_check = 0
    result = 0
    coins.sort(reverse=True)
    for i in coins:
        while see_check < sum_total:
            see_check += i
            result += 1
        if see_check == sum_total:
            return result
        see_check -= i
        result -= 1
    return -1