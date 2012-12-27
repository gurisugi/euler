#!/usr/bin/env python
#coding:utf-8

# basic way
ans = 0
for i in range(1000):
    if i%3 == 0 or i%5 == 0:
        ans += i
print ans

# one liner
print sum([i for i in range(1000) if i%3==0 or i%5==0])

