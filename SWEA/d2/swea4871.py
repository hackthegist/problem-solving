'''
4871. [파이썬 S/W 문제해결 기본] 4일차 - 그래프 경로
'''

import sys
sys.stdin = open("SWEA/inputs/4871_in.txt", "r")


def dfs(node):
    visited = [0] * (v + 1)
    stack = [0] * 20
    top = -1

    top += 1
    stack[top] = node

    while top > -1:
        # pop()
        popn = stack[top]
        top -= 1
        # visit
        if visited[popn] != 1:
            visited[popn] = 1
            # check adjacent nodes -> visit
            for i in range(1, v+1):
                if adj_t[popn][i] and not visited[i]:
                    if i == s:
                        return 1
                    top += 1
                    stack[top] = i
    return 0


t = int(input())
ans = ""

for i in range(1, t+1):
    v, e = map(int, input().split())
    edges = []
    for _ in range(e):
        edges += list(map(int, input().split()))
    s, g = map(int, input().split())

    adj_t = [[0] * (v + 1) for _ in range(v + 1)]
    for j in range(0, len(edges), 2):
        adj_t[edges[j+1]][edges[j]] += 1

    ans += "#{} {}\n".format(i, dfs(g))

    # ans += "#{} {}\n".format(i, result)

print(ans)
