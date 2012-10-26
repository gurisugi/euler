#!/usr/bin/env python
#coding:utf-8

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
"""

# stefan_yes's code
from math import *
import time

s = time.time()

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

def find_next_prime(prime):
    prime = incr(prime)
    while not is_prime(prime):
        prime = incr(prime)
    return prime

i=2
prime=3
while i < 10001:
    prime = find_next_prime(prime)
    i = i + 1
    print "Prime %d is %d\n" % (i, prime)

print time.time() - s
