#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 18:23:10 2024

@author: user2
"""


def gcd(inta, intb):
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

    if len(direct) < 2:
        return direct

    if direct[:2] in pairs:
        return remove_pairs(direct[2:])

    return direct[0] + remove_pairs(direct[1:])


def bisection_root(func, num1, num2):
    """function that applies the Bisection method given a function
    and two numbers"""

    fun1 = func(num1)
    fun2 = func(num2)
    close = 10 ** -7

    if (fun1 > 0 and fun2 < 0) or (fun1 < 0 and fun2 > 0):
        pass
    else:
        raise ValueError("Initial guesses do not bracket the root.")

    if abs(fun1) < close:
        return num1
    if abs(fun2) < close:
        return num2

    midp = (num1 + num2) / 2
    fun3 = func(midp)

    if (fun3 > 0 and fun1 < 0) or (fun3 < 0 and fun1 > 0):
        return bisection_root(func, num1, midp)
    return bisection_root(func, midp, num2)
