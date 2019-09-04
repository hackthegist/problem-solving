'''
4615. 재미있는 오셀로 게임
'''

import sys
sys.stdin = open("SWEA/inputs/4615_in.txt", "r")

def swipe(x, y, c):
    d = 2 if c == 1 else 1
    
    bg[x][y] = c
    for dx, dy in (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1),  (0, 1), (1, 1):
        i, j = x, y
        i += dx
        j += dy
        if not 0 <= i < n:
            continue 
        if not 0 <= j < n:
            continue 
        if bg[i][j] == d:
            flag = True
            while bg[i][j] == d:
                i += dx
                j += dy
                if not 0 <= i < n:
                    flag = False
                    break 
                if not 0 <= j < n:
                    flag = False
                    break
            if flag and bg[i][j] == c:
                i -= dx
                j -= dy
                while bg[i][j] == d:
                    bg[i][j] = c   
                    i -= dx
                    j -= dy
                    
t = int(input())
ans = ""

for tc in range(1, t+1):
    n, m = map(int, input().split())
    bg = [[0] * n for _ in range(n)]
    bg[n//2-1][n//2-1] = bg[n//2][n//2] = 2
    bg[n//2-1][n//2] = bg[n//2][n//2-1] = 1


    for _ in range(m):
        x, y, c = map(int, input().split())
        b_cnt = w_cnt = 0
        swipe(x-1, y-1, c)
    for i in range(n):
        for j in range(n):
            if bg[i][j] == 1:
                b_cnt += 1
            elif bg[i][j] == 2:
                w_cnt += 1
    res = "{} {}".format(b_cnt, w_cnt)

    ans += "#{} {}\n".format(tc, res)

print(ans)