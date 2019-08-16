'''
4861. [파이썬 S/W 문제해결 기본] 3일차 - 회문
'''

import sys
sys.stdin = open("SWEA/inputs/4861_in.txt", "r")

t = int(input())
for i in range(t):
    n, p = map(int, input().split())
    mat = []
    result = None

    for _ in range(n):
        row = input()

        for j in range(n-p+1):
            p_row = row[j:j+p]
            cmp = p//2 if p % 2 == 0 else p//2 + 1

            for k in range(cmp):
                if p_row[k] != p_row[p-k-1]:
                    break
            else:
                result = p_row
                break
        mat.append(row)

    for l in range(n):
        col = ""
        for k in range(n):
            col += mat[k][l]

        for j in range(n-p+1):
            p_col = col[j:j+p]
            cmp = p//2 if p % 2 == 0 else p//2 + 1

            for m in range(cmp):
                if p_col[m] != p_col[p-m-1]:
                    break
            else:
                result = p_col
                break

    print("#{} {}".format(i+1, result))
