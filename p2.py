#!/usr/bin/env python
#coding:utf-8

def solve(limit_n, first_n=1, second_n=2, ans=2):
    third_num = first_n + second_n

    if third_num % 2 == 0:
        ans = ans + third_num

    if third_num >= limit_n:
        return ans
    else:
        return solve(limit_n, second_n, third_num, ans)

if __name__ == '__main__':
    print solve(4000000)
