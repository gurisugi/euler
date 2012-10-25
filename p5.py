#!/usr/bin/env python
#coding:utf-8

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from collections import Counter

def solve(num, i, lis):
    while i <= num:
        if num % i == 0:
            lis.append(i)
            return solve(num/i, i, lis)
        else:
            i += 1
    return lis

if __name__ == '__main__':
    cnt = Counter()
    tmp_cnt = Counter()

    for num in range(2, 21):
        tmp_cnt.clear()
        for i in solve(num, 2, []):
            tmp_cnt[i] += 1

        for key in tmp_cnt.keys():
            if not key in cnt.keys() or cnt[key] < tmp_cnt[key]:
                cnt[key] = tmp_cnt[key]

    print reduce(lambda a,b: a*b, [key**cnt[key] for key in cnt.keys()])

# Iassevk's awesome code
# 小さい方から割り切れない数を見つけて倍数にしていく
# よくわからない日本語
    i = 1
    for k in (range(1, 21)):
        if i % k > 0:
            for j in range(1, 21):
                if (i*j) % k == 0:
                    i *= j
                    break
    print i
