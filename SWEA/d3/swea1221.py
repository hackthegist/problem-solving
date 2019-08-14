'''
1221. [S/W 문제해결 기본] 5일차 - GNS
'''

import sys
sys.stdin = open("SWEA/inputs/1221_in.txt", "r")

t = int(input())
for i in range(t):
    p, _ = input().split()
    nums = input().split()
    day_list = ["ZRO", "ONE", "TWO", "THR",
                "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    cnt_list = [0] * 10
    mat = [[0] * 100 for _ in range(100)]

    for k in range(len(day_list)):
        mat[ord(day_list[k][0])][ord(day_list[k][1])] = k

    for num in nums:
        cnt_list[mat[ord(num[0])][ord(num[1])]] += 1

    # for num in nums:
    #     cnt_list[diff_list.index(num)] += 1

    # for num in nums:
    #     for k, v in enumerate(diff_list):
    #         if num == v:
    #             cnt_list[k] += 1

    # for num in nums:
    #     for k, v in tp_list:
    #         if num == k:
    #             cnt_list[v] += 1
    #             break

    print(p)
    for j in range(10):
        print((day_list[j] + " ") * cnt_list[j], end="")
    print()

    #
    #     [print(diff_list[j], end=" ") for _ in range(cnt_list[j])]
