'''
4837. [파이썬 S/W 문제해결 기본] 2일차 - 부분집합의 합 
1) 부분집합 전체를 구한 후, (binary counting)
2) 합 필터링,
3) 부분집합 개수 필터링,
'''

import sys
sys.stdin = open("inputs/4837_in.txt", "r")


def get_sum(nums):
    s = 0
    for num in nums:
        s += num
    return s


def get_len(nums):
    cnt = 0
    for num in nums:
        cnt += 1
    return cnt


t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    a = list(range(1, 13))
    new = []
    cnt = 0

    # if n == 1
    for l in range(1 << 12):
        for j in range(12):
            if l & (1 << j):
                new.append(a[j])

        if get_len(new) == n and get_sum(new) == k:
            cnt += 1
        new = []

    print("#{} {}".format(i+1, cnt))


# t = int(input())
# for i in range(t):
#     n, k = map(int, input().split())
#     a = list(range(1, 13))
#     cnt_sub =

#     # if n == 1
#     for i in range(cnt_sub):
#         for j in range(n):
#             if i & (1 << j):
#                 new.append(arr[j])


#     print("#{} {}".format(i+1, result))
