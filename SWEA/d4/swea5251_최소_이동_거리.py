'''
5251. [파이썬 S/W 문제해결 구현] 7일차 - 최소 이동 거리
'''

import sys
sys.stdin = open("SWEA/inputs/5251_in.txt", "r")

ans = ""

for tc in range(1, int(input())+1):
    n, e = map(int, input().split())
    edges = {k: [0]*(n+1) for k in range(0, n+1)}
    for a, b, w in [map(int, input().split()) for _ in range(e)]:
        edges[a][b] = w
    visit = [0] * (n+1)
    dsts = [float('inf')] * (n+1)

    node = dsts[node] = res = 0
    to_go = None
    
    while node != n:
        visit[node] = 1
        for d in range(n+1):
            if edges[node][d] and edges[node][d] + dsts[node] < dsts[d]: 
                dsts[d] = edges[node][d] + dsts[node]
        mn = 1000
        for i in range(len(edges[node])):
            if not visit[i] and dsts[i] < mn:
                to_go = i
                mn = dsts[i]
        node = to_go
        res = dsts[n]


    ans += "#{} {}\n".format(tc, res)

print(ans)