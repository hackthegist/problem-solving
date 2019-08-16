'''
1215. [S/W 문제해결 기본] 3일차 - 회문1
'''

import sys
sys.stdin = open("SWEA/inputs/1215_in.txt", "r")

# t = 10
# for i in range(t):
#     n = int(input())
#     mat = [list(input()) for _ in range(8)]
#     cnt = 0

#     for row in mat:
#         for j in range(9 - n):
#             p_row = row[j:j+n]
#             if p_row == p_row[::-1]:
#                 cnt += 1

#     for col in [[row[k] for row in mat] for k in range(8)]:
#         for j in range(9 - n):
#             p_col = col[j: j+n]
#             if p_col == p_col[::-1]:
#                 cnt += 1

#     print("#{} {}".format(i+1, cnt))

# 2 string으로 다루기
# t = 10
# for i in range(t):
#     n = int(input())
#     mat = [input() for _ in range(8)]
#     cnt = 0

#     for row in mat:
#         for j in range(9 - n):
#             p_row = row[j:j+n]
#             if p_row == p_row[::-1]:
#                 cnt += 1

#     for j in range(8):
#         col = ""
#         for k in range(8):
#             col += mat[k][j]
#         for l in range(9 - n):
#             p_col = col[l: l+n]
#             if p_col == p_col[::-1]:
#                 cnt += 1

#     print("#{} {}".format(i+1, cnt))

# 3 행을 스트림으로 처리하기
t = 10
for i in range(t):
    n = int(input())
    cnt = 0
    mat = []

    for _ in range(8):
        row = input()
        for j in range(9 - n):
            p_row = row[j:j+n]
            if p_row == p_row[::-1]:
                cnt += 1
        mat.append(row)

    for j in range(8):
        col = ""
        for k in range(8):
            col += mat[k][j]
        for l in range(9 - n):
            p_col = col[l: l+n]
            if p_col == p_col[::-1]:
                cnt += 1

    print("#{} {}".format(i+1, cnt))
