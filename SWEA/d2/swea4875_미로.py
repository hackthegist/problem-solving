'''
4875. [파이썬 S/W 문제해결 기본] 5일차 - 미로
'''

import sys
sys.stdin = open("SWEA/inputs/4875_in.txt", "r")



t = int(input())
ans = ""

for i in range(1, t+1):
    n = int(input())
    # nums = [input() for _ in range(n)]
    nums = [list(input()) for _ in range(n)]
    memo = []
    result = 0

    for j in range(n):
        for k in range(n):
            if nums[j][k] == "2":
                x, y = j, k

    sol(x, y)

    ans += "#{} {}\n".format(i, result)

print(ans)
