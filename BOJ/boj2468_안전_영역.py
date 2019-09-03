'''
Olympiad > 한국정보올림피아드 > KOI 2010 > 초등부 2번
2468. 안전 영역
'''

import sys
sys.stdin = open("BOJ/inputs/2468_in.txt", "r")


def dfs(i, j):
    stack = []
    stack.append((i, j))
    nums[i][j] =

    while stack:
        for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            x += i
            y += j
            if x < 0 or x > n-1:
                continue
            if y < 0 or y > n-1:
                continue
            if nums[x][y]:
                stack.append((x,y))
            while stack:

mx = 0
n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

mx_h = 0
for num in nums:
    mx_h = max(num) if max(num) > mx_h else mx_h

for h in range(1, mx_h+1):
    for i in range(n):
        for j in range(n):
            if nums[i][j] < h:
                num[i][j] = 0
    stack = []
    for i in range(n):
        for j in range(n):
            if nums[i][j]:
                



ans += "#{} {}\n".format(tc, res)

print(ans)