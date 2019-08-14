'''
4836. [파이썬 S/W 문제해결 기본] 2일차 - 색칠하기
'''

import sys
sys.stdin = open("SWEA/inputs/4836_in.txt", "r")

t = int(input())
for i in range(t):
    n = int(input())
    cnt_tb = [[0 for _ in range(10)] for _ in range(10)]
    # [[0]*10 for _ in range(10)]
    cnt = 0

    for _ in range(n):
        nums = list(map(int, input().split()))
        x1, y1, x2, y2, color = nums[0], nums[1], nums[2], nums[3], nums[4]
        # x1, y1, x2, y2, color = map(int, input().split())
        inc = 1 if color == 1 else 10

        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                cnt_tb[x][y] += inc

    for x in cnt_tb:
        for cell in x:
            if cell >= 11 and cell % 10 != 0:
                cnt += 1

    print("#{} {}".format(i+1, cnt))
