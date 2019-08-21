'''
1210. [S/W 문제해결 기본] 2일차 - Ladder1
'''

import sys
sys.stdin = open("SWEA/inputs/1210_in.txt", "r")


# ans = ""

# for i in range(1, 11):
#     t = int(input())
#     bg = [list(map(int, input().split())) for _ in range(100)]
#     cols = [j for j in range(len(bg[99])) if bg[99][j]]
#     y_idx = cols.index(bg[99].index(2))
#     x, y = 99, cols[y_idx]

#     while x > 0:
#         x -= 1

#         if y != 0 and bg[x][y-1] == 1:
#             y_idx -= 1
#             y = cols[y_idx]

#         elif y != 99 and bg[x][y+1] == 1:
#             y_idx += 1
#             y = cols[y_idx]

#     ans += "#{} {}\n".format(i, y)

# print(ans)

ans = ""

for i in range(1, 11):
    t = int(input())
    bg = [list(map(int, input().split())) for _ in range(100)]
    cols = [j for j in range(len(bg[99])) if bg[99][j]]
    y_idx = cols.index(bg[99].index(2))
    x, y = 99, cols[y_idx]

    while x > 0:
        x -= 1

        if y != 0 and bg[x][y-1] == 1:
            y_idx -= 1
            y = cols[y_idx]

        elif y != 99 and bg[x][y+1] == 1:
            y_idx += 1
            y = cols[y_idx]

    ans += "#{} {}\n".format(i, y)
