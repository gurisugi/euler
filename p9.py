#!/usr/bin/env python
#coding:utf-8

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import time

t = time.time()

for a in range(998):
    for b in range(a+1, 998):
        if a + b > 1000: break
        for c in range(b+1, 998):
            if a + b + c > 1000: break
            if (a + b + c == 1000) and (a**2 + b**2 == c**2):
                print a*b*c

print time.time() - t
