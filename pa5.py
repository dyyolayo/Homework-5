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
        return gcd(intb, inta%intb)
    if intb >= inta:
        return gcd(inta, intb%inta)

def remove_pairs(direct):
    """remove pairs of directions which undo each other"""
    ret = direct.split
    return ret

print(remove_pairs("EEWWNWS"))