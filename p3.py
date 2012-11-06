#!/usr/bin/env python
#coding:utf-8

"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

def solve(num, i=2, lis=None):
    while i <= num:
        if lis == None: lis = []
        if num % i == 0:
            lis.append(i)
            return solve(num/i, i, lis)
        else:
            i += 1
    return max(lis)

if __name__ == '__main__':
    num = 600851475143
    print solve(num)

