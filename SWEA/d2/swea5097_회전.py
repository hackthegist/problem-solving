'''
5097. [파이썬 S/W 문제해결 기본] 6일차 - 회전
'''

import sys
sys.stdin = open("SWEA/inputs/5097_in.txt", "r")

t = int(input())
ans = ""

for tc in range(1, t+1):
    n, m = map(int, input().split())
    nums = input().split()
    index = m % n
    res = nums[index]


    ans += "#{} {}\n".format(tc, res)

print(ans)