'''
4865. [파이썬 S/W 문제해결 기본] 3일차 - 글자수
'''

import sys
sys.stdin = open("SWEA/inputs/4865_in.txt", "r")

t = int(input())
for i in range(t):
    short, long = input(), input()
    cnt_dict = {}

    for sh in short:
        if sh not in cnt_dict.keys():
            cnt_dict[sh] = 0
    for lg in long:
        if lg in cnt_dict.keys():
            cnt_dict[lg] += 1
    mx = 0
    for k, v in cnt_dict.items():
        if v > mx:
            mx = v

    print("#{} {}".format(i+1, mx))
