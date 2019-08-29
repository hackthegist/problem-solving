'''
5102. [파이썬 S/W 문제해결 기본] 6일차 - 노드의 거리
'''

import sys
sys.stdin = open("SWEA/inputs/5102_in.txt", "r")

def bfs(g, n, e, s, l):
    queue = []
    visited = [0] * (n+1)
    cnt = 0
    queue.append(s)

    while queue:
        n_queue = len(queue)
        cnt += 1
        for _ in range(n_queue):
            dq = queue.pop(0)
            if not visited[dq]:
                visited[dq] = 1
            for next_ in g[dq]:
                if next_ == l:
                    return cnt
                if not visited[next_] and next_ not in queue:
                    queue.append(next_)
    return 0
        
t = int(input())
ans = ""

for tc in range(1, t+1):
    v, e = map(int, input().split())
    g = {}
    for i in range(v+1):
        g[i] = []
    for _ in range(e):
        from_, to = map(int, input().split())
        g[from_].append(to)
        g[to].append(from_) 
    s, l = map(int, input().split())

    res = bfs(g, v, e, s, l)
    if l == s:
        res = 0

    ans += "#{} {}\n".format(tc, res)

print(ans)