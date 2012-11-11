#! /usr/bin/env python
#coding:utf-8

"""problem
The following iterative sequence is defined for the set of positive integers:

n  n/2 (n is even)
n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def collatz(num):
    lis = []
    lis.append(num)
    while not num == 1 and not num == 0:
        if num%2 == 0:
            num = num/2
            lis.append(num)
        else:
            num = 3*num+1
            lis.append(num)
    return lis


def main():
    ans = 0
    max_collatz = 0
    for i in range(1,1000000):
        len_coll = collatz(i)
        if max_collatz < len_coll:
            max_collatz = len_coll
            ans = i
    print ans

if __name__ == '__main__':
    main()
