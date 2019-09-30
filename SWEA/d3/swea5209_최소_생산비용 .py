'''
5209. [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용
'''

import sys
sys.stdin = open("SWEA/inputs/5209_in.txt", "r")

def process(visited, v, s):
    global res
    visited = visited[:]

    if s >= res:
        return
    if v == n:
        res = s if res > s else res
        return 
    
    for i in range(n):
        if visited[i]:
            visited[i] = 0
            process(visited, v+1, s+nums[v][i])
            visited[i] = 1


t = int(input())
ans = ""

for i in range(1, t+1):
    n = int(input())
    nums = [[*map(int, input().split())] for _ in range(n)]
    res = (n ** 2) * 99

    process([1] * n, 0, 0)

    ans += "#{} {}\n".format(i, res)

print(ans)