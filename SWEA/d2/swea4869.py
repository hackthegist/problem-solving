'''
4869. [파이썬 S/W 문제해결 기본] 4일차 - 종이붙이기

역으로 생각하면 10이 부족한 경우, 20이 부족한 경우 * 2가 있다 -> 점화식
'''

import sys
sys.stdin = open("SWEA/inputs/4869_in.txt", "r")


def get_parts(n):
    if n == 20:
        return 3
    if n == 10:
        return 1
    return get_parts(n-10) + 2 * get_parts(n-20)


t = int(input())
ans = ""

for i in range(1, t+1):
    n = int(input())
    cnt = 0

    ans += "#{} {}\n".format(i, get_parts(n))

print(ans)
