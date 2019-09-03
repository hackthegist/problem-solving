'''
5108. [파이썬 S/W 문제해결 기본] 7일차 - 숫자 추가
'''

import sys
sys.stdin = open("SWEA/inputs/5108_in.txt", "r")

t = int(input())
ans = ""

for tc in range(1, t+1):
    n, m, l = map(int, input().split())
    nums = list(map(int, input().split()))
    for _ in range(m):
        idx, num = map(int, input().split())
        nums.insert(idx, num)
    res = str(nums[l])
    ans += "#{} {}\n".format(tc, res)

print(ans)