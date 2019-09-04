'''
브루트 포스
14889. 스타트와 링크
브루트 포스
'''

import sys
sys.stdin = open("BOJ/inputs/14889_in.txt", "r")

for tc in range(3):
    n = int(input())
    stats = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n-i):
            stats[i][j] = stats[i][j] + stats[j][i]
            stats[j][i] = stats[i][j]

    # mn = 100
    # players = list(range(1, n+1))
    # p = 2**(n//2)
    # for i in range(p-1, (p-1)<<p):
    #     t1 = []
    #     t1_score = 0
    #     t2 = []
    #     t2_score = 0
    #     for j in range(n):
    #         if i & (1<<j):
    #             t1.append(players[j])
    #         else:
    #             t2.append(players[j])
    #     for l in range(n//2-1):
    #         for m in range(l, n//2):
    #             t1_score += stats[l][m]
    #             t2_score += stats[l][m]
    #     mn = abs(t1_score - t2_score) if abs(t1_score - t2_score) < mn else mn
    
    # print(mn)