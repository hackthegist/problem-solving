'''
1216. [S/W 문제해결 기본] 3일차 - 회문2

1. 가로세로 모든 회문을 조사
2. 회문의 길이를 측정해 최대 길이를 갱신
'''

import sys
sys.stdin = open("SWEA/inputs/1216_in.txt", "r")

# 1
# t = 10
# for i in range(t):
#     n = int(input())
#     mat = [list(input()) for _ in range(100)]
#     s = 0
#     mx = 0

#     for row in mat:
#         for j in range(99):
#             for k in range(j+1, 100):
#                 if row[j] == row[k] and row[j:k+1] == row[j:k+1][::-1]:
#                     for _ in row[j:k+1]:
#                         s += 1
#                     mx = s if mx < s else mx
#                 s = 0

#     for col in [[row[k] for row in mat] for k in range(100)]:
#         for j in range(99):
#             for k in range(j+1, 100):
#                 if col[j] == col[k] and col[j:k+1] == col[j:k+1][::-1]:
#                     for _ in col[j:k+1]:
#                         s += 1
#                     mx = s if mx < s else mx
#                 s = 0

#     print("#{} {}".format(i+1, mx))

# 2 회둔 조사 이전에 배열의 길이로 break
# t = 10
# for i in range(t):
#     n = int(input())
#     mat = [list(input()) for _ in range(100)]
#     s = 0
#     mx = 0

#     for row in mat:
#         for j in range(99):
#             for k in range(j+1, 100):
#                 if k - j > mx and row[j] == row[k] and row[j:k+1] == row[j:k+1][::-1]:
#                     for _ in row[j:k+1]:
#                         s += 1
#                     mx = s if mx < s else mx
#                 s = 0

#     for col in [[row[k] for row in mat] for k in range(100)]:
#         for j in range(99):
#             for k in range(j+1, 100):
#                 if k - j and col[j] == col[k] and col[j:k+1] == col[j:k+1][::-1]:
#                     for _ in col[j:k+1]:
#                         s += 1
#                     mx = s if mx < s else mx
#                 s = 0

#     print("#{} {}".format(i+1, mx))

# 3 string으로 다루기
# t = 10
# for i in range(t):
#     n = int(input())
#     mat = [input() for _ in range(100)]
#     s = 0
#     mx = 0

#     for row in mat:
#         for j in range(99):
#             for k in range(j+1, 100):
#                 if k - j > mx and row[j] == row[k] and row[j:k+1] == row[j:k+1][::-1]:
#                     for _ in row[j:k+1]:
#                         s += 1
#                     mx = s if mx < s else mx
#                 s = 0
#     for j in range(100):
#         col = ""
#         for k in range(100):
#             col += mat[k][j]
#         for l in range(99):
#             for m in range(l+1, 100):
#                 if m - l and col[l] == col[m] and col[l:m+1] == col[l:m+1][::-1]:
#                     for _ in col[l:m+1]:
#                         s += 1
#                     mx = s if mx < s else mx
#                 s = 0

#     print("#{} {}".format(i+1, mx))

# 4 원소 단위별 비교
t = 10
for i in range(t):
    n = int(input())
    mat = [input() for _ in range(100)]
    mx = 0

    for row in mat:
        for j in range(99):
            for k in range(j+1, 100):
                ln = k-j+1
                if ln > mx and row[j] == row[k]:
                    p_row = row[j:k+1]
                    cmp = ln//2 if ln % 2 == 0 else ln//2 + 1
                    for n in range(cmp):
                        if p_row[n] != p_row[ln-n-1]:
                            break
                    else:
                        mx = ln

    for j in range(100):
        col = ""
        for k in range(100):
            col += mat[k][j]
        for l in range(99):
            for m in range(l+1, 100):
                ln = m-l+1
                if ln > mx and col[l] == col[m]:
                    p_col = col[l:m+1]
                    cmp = ln//2 if ln % 2 == 0 else ln//2 + 1
                    for n in range(cmp):
                        if p_col[n] != p_col[ln-n-1]:
                            break
                    else:
                        mx = ln

    print("#{} {}".format(i+1, mx))

# 5 큰 수부터 줄어들며 찾기
