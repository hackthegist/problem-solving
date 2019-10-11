'''
5176. [파이썬 S/W 문제해결 기본] 8일차 - 이진탐색
'''

import sys
sys.stdin = open("SWEA/inputs/5176_in.txt", "r")

ans = ""

for tc in range(1, int(input())+1):
    n = int(input())

    full_cnt = 1
    while 2**full_cnt - 1 < n:
        full_cnt += 1
    prev_mx = 2**(full_cnt - 1) - 1
    next_mx = 2**full_cnt - 1

    if n < prev_mx + (next_mx - prev_mx)//2:
        root = n - (prev_mx - 1) // 2
        rest = n - prev_mx
        if rest % 2 == 0:
            rest -= 1
        rest *= 2
    elif n > prev_mx + (next_mx - prev_mx)//2:
        root = (next_mx - 1)//2 + 1
        rest = n - (prev_mx + (next_mx - prev_mx)//2)
        if rest % 2 == 0:
            rest -= 1
        rest = 2*rest + root
    else:
        root = n
        rest = 0

    res = str(root) + " " + str(rest)
    ans += "#{} {}\n".format(tc, res)

print(ans)