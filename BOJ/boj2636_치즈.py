'''
Olympiad > 한국정보올림피아드 > KOI 2000 > 초등부 3번
2636. 치즈
'''

import sys
from pprint import pprint
sys.stdin = open("BOJ/inputs/2636_in.txt", "r")

# def bfs(g, x, y):
#     q = []
#     moves = [(1, 0), (0, -1), (-1, 0), (0, 1)]
#     q.append(x, y)
   
#     while q:
#         i, j = q.pop(0)
#         if bg[i][j] == 0:
#             for j, k in moves:
#                 j += i
#                 k += j

#         if bg[i][j] == 0:
#             for 

r, c = map(int, input().split())
bg = [list(map(int, input().split())) for _ in range(r)]

search = []
melting = []
search.append((0, 0))

while 
    while search:
        dq_x, dq_y = search.pop(0)
        if bg[dq_x][dq_y] == 0:
            bg[dq_x][dq_y] = 2
            for x, y in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                x += dq_x
                if x < 0 or x > r-1:
                    continue
                y += dq_y
                if y < 0 or y > c-1:
                    continue
                if bg[x][y] == 0 and bg[x][y] != 2:
                    search.append((x, y))
                if bg[x][y] == 1:
                    melting.append((x, y))

    melting = list(set(melting))
    search = melting[:]
    while melting:
        dq_x, dq_y = melting.pop(0)
        bg[dq_x][dq_y]



print(len(melting))


# for b in range(1, c-2):
#     if bg[1][b] == 0:
#         sx = 1
#         sy = b
#         break



# while not done:
#     for i in range(1, r-1):
#         for j in range(1, c-1):
#             if bg[i][j] == 0:
#                 if i == 1 or i == r-2 or j == 1 or j == c-2:
#                     bg[i][j] = 2
#                 for x, y in moves:
#                     x += i
#                     y += j
#                     if x < 1 or x > r-2:
#                         continue
#                     if y < 1 or y > c-2:
#                         continue
#                     if bg[x][y] == 2:
#                         bg[i][j] = 2
#                         break
#     else:
#         done = True
# pprint(bg)

# while cnt:
#     step += 1
#     cnt = one_step(bg, r, c)

# print(s)
# pprint(bg)
