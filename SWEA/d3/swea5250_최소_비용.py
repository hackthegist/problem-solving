'''
5250. [파이썬 S/W 문제해결 구현] 7일차 - 최소 비용
'''

import sys
sys.stdin = open("SWEA/inputs/5250_in.txt", "r")

ans = ""

for tc in range(1, int(input())+1):
    n = int(input())
    area = [list(map(int, input().split())) for _ in range(n)]
    move = [(1, 0), (0, 1), (-1, 0)]
    d = [[float('inf')]*n for _ in range(n)]
    vt = [[0]*n for _ in range(n)]

    d[0][0] = 0
    
    res = 0
    x = y = 0
    while x != n-1 or y != n-1:
        mc = float('inf')
        vt[x][y] = 1
        res += d[x][y]
        for dx, dy in move:
            dx += x
            dy += y
            if not 0 <= dx < n:
                continue
            if not 0 <= dy < n:
                continue
            if vt[dx][dy]:
                continue

            if d[dx][dy] > 1 + (area[dx][dy] - area[x][y]) + d[x][y]:
                d[dx][dy] = 1 + (area[dx][dy] - area[x][y] + d[x][y])
                if dx == n-1 and dy == n-1:
                    minx, miny = dx, dy
                    break
            if d[dx][dy] < mc:
                minx = dx
                miny = dy
                mc = d[dx][dy]
        x, y = minx, miny

    res = d[n-1][n-1]
    print("#{} {}".format(tc, res))
    # ans += "#{} {}\n".format(tc, res)

print(ans)