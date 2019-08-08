'''
4843. [파이썬 S/W 문제해결 기본] 2일차 - 특별한 정렬
'''

import sys
sys.stdin = open("inputs/4843_in.txt", "r")


def min_idx(nums):
    mn, mn_idx = nums[0], 0
    for i in range(len(nums)):
        if mn > nums[i]:
            mn, mn_idx = nums[i], i
    return mn_idx


def max_idx(nums):
    mx, mx_idx = nums[0], 0
    for i in range(len(nums)):
        if mx < nums[i]:
            mx, mx_idx = nums[i], i
    return mx_idx


t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    for j in range(n):
        mx_idx, mn_idx = max_idx(nums[j:]), min_idx(nums[j:])
        if j % 2 == 0:
            nums[j], nums[mx_idx+j] = nums[mx_idx+j], nums[j]
        else:
            nums[j], nums[mn_idx+j] = nums[mn_idx+j], nums[j]

    print("#{}".format(i+1), end=" ")
    [print(nums[x], end=" ") for x in range(10)]
    print()
