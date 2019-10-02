'''
7465. 창용 마을 무리의 개수
'''

import sys
sys.stdin = open("SWEA/inputs/7465_in.txt", "r")


ans = ""

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    conn = {x: [] for x in range(1, n+1)}
    res = 0

    for _ in range(m):

        fr, to = map(int, input().split())
        conn[fr].append(to)
        conn[to].append(fr)

    visited = [0] * (n+1)
    q = []
    q.append(1)
    while sum(visited) < n:
        while q:
            dq = q.pop(0)
            visited[dq] = 1
            for c in conn[dq]:
                if not visited[c] and c not in q:
                    q.append(c)
        res += 1

        for j in range(1, n+1):
            if not visited[j]:
                q.append(j)
                break

    ans += "#{} {}\n".format(tc, res)

print(ans)