#!/usr/bin/env python3
"""This script defines a function to calculate the minimum number of operation"""

def minOperations(n):
    """
    Calculate the minimum number of operations

    The operations allowed are:
    1. Copy All: Copies all characters in the file.
    2. Paste: Pastes the copied characters.
    Args:
    n (int): The target number of 'H' characters.
    Returns:
    int: The minimum number of operations.
    """
    
    # If n is less than or equal to 1, it's impossible to achieve n 'H'.
    if n <= 1:
        return 0
    
    # Initialize the number of operations required.
    task = 0
    
    # Start with the smallest possible factor, which is 2.
    done_task = 2
    
    # Continue the process until n reduces to 1.
    while n > 1:
        # While n is divisible by the current factor, reduce n.
        while n % done_task == 0:
            task += done_task
            n /= done_task
        # Move to the next potential factor.
        done_task += 1
    
    return task
