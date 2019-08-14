'''
1215. [S/W 문제해결 기본] 3일차 - 회문1
'''

import sys
sys.stdin = open("SWEA/inputs/1215_in.txt", "r")

t = 10
for i in range(t):
    n = int(input())
    mat = [list(input()) for _ in range(8)]
    cnt = 0

    for row in mat:
        for j in range(9 - n):
            p_row = row[j:j+n]
            if p_row == p_row[::-1]:
                cnt += 1

    for col in [[row[k] for row in mat] for k in range(8)]:
        for j in range(9 - n):
            p_col = col[j: j+n]
            if p_col == p_col[::-1]:
                cnt += 1

    print("#{} {}".format(i+1, cnt))
