from pprint import pprint

gl = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
n = len(gl)//2

g = [[0]*(n+1) for _ in range(n+1)]
for i in gl[::2]:
    g[i][i+1] = 1
    g[i+1][i] = 1

def bfs(g, v):
    visited = [0] * n
    queue = []
    queue.append(v)

    while queue:
        t = queue.pop(0)
        if not visited[t]:
            visited[t] = 1
            visit(t)
        for i in range(1, n+1):
            if g[t][i] and not visited[i]:
                queue.append(i)

def visit(v):
    print(v, end=" ")

bfs(g, 1)