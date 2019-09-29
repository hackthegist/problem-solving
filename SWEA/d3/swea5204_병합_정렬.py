'''
5204. [파이썬 S/W 문제해결 구현] 4일차 - 병합 정렬
'''

import sys
sys.stdin = open("SWEA/inputs/5204_in.txt", "r")

def merge_sort(lst):

    length = len(lst)
    if length == 1:
        return lst
    
    left = lst[:length//2]
    right = lst[length//2:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    global result
    res = []
    i = j = 0

    while i < len(left) or j < len(right):
        if i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        elif j < len(right):
            res += right[j:]
            j = len(right)
        elif i < len(left):
            res += left[i:]
            i = len(left)
            result += 1
    return res

t = int(input())
ans = ""

for i in range(1, t+1):
    n = int(input())
    nums = list(map(int, input().split()))
    result = 0
    middle = merge_sort(nums)[n//2]

    ans += "#{} {} {}\n".format(i, middle, result)

print(ans)