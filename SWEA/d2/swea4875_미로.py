'''
4875. [파이썬 S/W 문제해결 기본] 5일차 - 미로
'''

import sys
sys.stdin = open("SWEA/inputs/4875_in.txt", "r")



import sys
sys.stdin = open("SWEA/inputs/5105_in.txt", "r")

def dfs(g, n, s):
    stack = []
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    stack.append(s)

    while stack:
        pop_ = stack.pop()
        if g[pop_[0]][pop_[1]] == "0":
            g[pop_[0]][pop_[1]] = "1"
        for x, y in moves:
            x += pop_[0]
            y += pop_[1]
            if g[x][y] == "0":
            if g[x][y] == "0":
                stack.append([x, y])


            
        
        nq = len(q)
        cnt += 1
        for _ in range(nq):
            dq = q.pop(0)
            if g[dq[0]][dq[1]] == "0":
                g[dq[0]][dq[1]] = 1
            for x, y in moves:
                x += dq[0]
                y += dq[1]
                if x < 0 or x > n-1:
                    continue
                if y < 0 or y > n-1:
                    continue
                if g[x][y] == "0":
                    q.append([x, y])
                elif g[x][y] == "3":
                    return cnt-1
                else:
                    continue
    return 0


            

t = int(input())
ans = ""

for tc in range(1, t+1):
    n = int(input())
    bg = [list(input()) for _ in range(n)]

    for i in range(n):
        if "2" in bg[i]:
            x = i
    y = bg[x].index("2")

    res = dfs(bg, n, [x,y])

    ans += "#{} {}\n".format(tc, res)

print(ans)