#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 18:23:10 2024

@author: user2
"""

def gcd(inta,intb):
    if inta == 0:
        return intb
    if intb == 0:
        return inta 
    if inta >= intb:
        return gcd(intb, inta%intb)
    if intb >= inta:
        return gcd(inta, intb%inta)
    
gcd(5,21)

