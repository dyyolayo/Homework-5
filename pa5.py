#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 18:23:10 2024

@author: user2
"""


def gcd(inta,intb):
    """function created to take the greatest common divisor of two integers"""
    if inta == 0:
        return intb
    if intb == 0:
        return inta
    if inta >= intb:
        return gcd(intb, inta % intb)
    if intb >= inta:
        return gcd(inta, intb % inta)


def remove_pairs(direct):
    """Remove pairs of directions which undo each other"""

    pairs = ["EW", "WE", "NS", "SN"]

    for a in range(len(direct) - 1):
        if direct[a : a + 2] in pairs:
            new = direct[:a] + direct[a+ 2:]
            return new
    return direct


def bisection_root(func, x1, x2):
    # Check if the initial guesses have different signs
    if func(x1) * func(x2) >= 0:
        raise ValueError("Initial guesses do not bracket the root.")

    # Define the tolerance for y-value close to zero
    tolerance = 10**(-7)

    # Loop until the y-value of one of the x-values is close to zero
    while True:
        # Calculate the midpoint between the two x-values
        x_mid = (x1 + x2) / 2
        # Calculate the y-value at the midpoint
        y_mid = func(x_mid)

        # Check if the y-value at the midpoint is close to zero
        if abs(y_mid) < tolerance:
            return x_mid  # Return the midpoint as the root

        # Update the x-values based on the signs of the y-values
        if func(x1) * y_mid < 0:
            x2 = x_mid  # Update x2 if the signs differ
        else:
            x1 = x_mid  # Update x1 if the signs differ

        # Check if the interval is too small
        if abs(x2 - x1) < tolerance:
            return x_mid  # Return the midpoint as the root

# Test the function with math.sin and initial guesses 2 and 4
import math
root = bisection_root(math.sin, 2, 4)
print(root)  # Output: Approximately 3.141592653589793 (pi)

    