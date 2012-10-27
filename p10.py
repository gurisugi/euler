#!/usr/bin/env python
#coding:utf-8

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

from math import *

def is_prime(number):
    sqrt_nr = ceil(sqrt(number))
    i = 2
    while i <= sqrt_nr:
        if not(number % i) and (i != number):
            return False
        i = incr(i)
    return True

def incr(i):
    if i <= 2:
        return i + 1
    else:
        # do not search even number
        return i + 2

num = 2000000
ans = 0
p = 2
while p < num:
    if is_prime(p):
        ans += p
    p += 1
print ans
