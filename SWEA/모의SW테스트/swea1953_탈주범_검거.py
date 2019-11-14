'''
1953. [모의 SW 역량테스트] 탈주범 검거
'''

import sys
sys.stdin = open("SWEA/inputs/1953_in.txt", "r")

ans = ""

def pipe(x, y, p):
    right, bottom, left, top = [(0,1), (1,0), (0,-1), (-1,0)]
    res.add((x,y))
    ne = []
    tunnel[x][y] = -1

    if p == 1:
        moves = [right, bottom, left, top]
    elif p == 2:
        moves = [bottom, top]
    elif p == 3:
        moves = [left, right]
    elif p == 4:
        moves = [top, right]
    elif p == 5:
        moves = [bottom, right]
    elif p == 6:
        moves = [bottom, left]
    elif p == 7:
        moves = [top, left]
    else:
        return
    
    for mv in moves:
        dx, dy = mv
        dx += x
        dy += y
        if not 0 <= dx < n:
            continue
        if not 0 <= dy < m:
            continue
        if not tunnel[dx][dy]:
            continue
        if tunnel[dx][dy] not in conn[mv]:
            continue
        ne.append((dx, dy))
        

    return ne


for tc in range(1, int(input())+1):
    n, m, r, c, l = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(n)]
    conn = {
        (-1,0): [1, 2, 5, 6],
        (1,0): [1, 2, 4, 7],
        (0,-1): [1, 3, 4, 5],
        (0,1): [1, 3, 6, 7]
    }
    
    res = set()
    res.add((r,c))
    nexts = [(r,c)]
    
    for t in range(l-1):
        ln = len(nexts)
        for x, y in nexts[:ln]:
            ne = pipe(x, y, tunnel[x][y])
            if ne:
                nexts += ne
                res.update(nexts)
        nexts = nexts[ln:]

    res = len(res)
    ans += "#{} {}\n".format(tc, res)

print(ans)