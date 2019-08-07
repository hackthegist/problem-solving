'''
4835. [파이썬 S/W 문제해결 기본] 1일차 - 구간합
'''
import sys
sys.stdin = open("../inputs/4835_in.txt", "r")

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    mn = 10000 * m
    mx = m

    for j in range(n-m+1):
        s = 0
        for k in range(j, j+m):
            s += nums[k]
        mn = s if s < mn else mn
        mx = s if s > mx else mx

    print("#{} {}".format(i+1, mx - mn))


# avoid recomputing / use sliding window  (나중에 string manipulation에 활용)


# use accumulated list
