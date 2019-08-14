'''
1216. [S/W 문제해결 기본] 3일차 - 회문2
'''

import sys
sys.stdin = open("SWEA/inputs/1216_in.txt", "r")

t = 1
for i in range(t):
    n = int(input())
    mat = [list(input()) for _ in range(100)]
    s = 0
    mx = 0

    for row in mat:
        for j in range(99):
            for k in range(j+1, 100):
                if row[j] == row[k] and row[j:k+1] == row[j:k+1][::-1]:
                    print(row[j:k+1])
                    for _ in row[j:k+1]:
                        s += 1
                    mx = s if mx < s else mx
                    s = 0

    # for col in [[row[k] for row in mat] for k in range(100)]:
    #     for j in range(99):
    #         for k in range(j+1, 100):
    #             if row[j] == row[k] and row[j:k+1] == row[j:k+1][::-1]:
    #                 for _ in row[j:k+1]:
    #                     s += 1
    #                 mx = s if mx < s else mx
    #                 s = 0

    print("#{} {}".format(i+1, mx))
