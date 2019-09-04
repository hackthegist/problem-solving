'''
Olympiad > 한국정보올림피아드 > 한국정보올림피아드시․도지역본선 > 지역본선 2004 > 초등부 3번
2606. 바이러스
'''

import sys
sys.stdin = open("BOJ/inputs/2606_in.txt", "r")

n = int(input())
m = int(input())
con = {k: [] for k in range(1, n+1)}

for _ in range(m):
    from_, to = map(int, input().split())
    con[from_].append(to)
    con[to].append(from_)

cnt = 0
visited = [0] * (n+1)
q = []
q.append(1)

while q:
    dq = q.pop(0)
    if not visited[dq]:
        visited[dq] = 1
        cnt += 1
    if con[dq]:
        for node in con[dq]:
            if not visited[node] and node not in q:
                q.append(node)
print(cnt-1)