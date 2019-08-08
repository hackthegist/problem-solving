'''
4839. [파이썬 S/W 문제해결 기본] 2일차 - 이진탐색
'''

import sys
sys.stdin = open("inputs/4839_in.txt", "r")


def bisect_cnt(first, last, tg):
    if first > last:
        first, last = last, first
    m = (first + last) // 2
    cnt = 1

    while m != tg:
        if tg > m:
            first = m
        else:
            last = m
        cnt += 1
        m = (first + last) // 2
    return cnt


t = int(input())
for i in range(t):
    p, a, b = map(int, input().split())
    cnt_a, cnt_b = bisect_cnt(1, p, a), bisect_cnt(1, p, b)

    if cnt_a < cnt_b:
        result = "A"
    elif cnt_a > cnt_b:
        result = "B"
    else:
        result = 0

    print("#{} {}".format(i+1, result))
