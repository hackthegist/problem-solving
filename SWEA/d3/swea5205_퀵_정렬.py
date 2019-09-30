'''
5205. [파이썬 S/W 문제해결 구현] 4일차 - 퀵 정렬
'''

import sys
sys.stdin = open("SWEA/inputs/5205_in.txt", "r")

def quicksort(arr, l, r):
    if l < r:
        s = partition(arr, l, r)
        quicksort(arr, l, s - 1)
        quicksort(arr, s + 1, r)

def partition(arr, l, r):
    p = arr[l]
    i, j = l, r
    while i <= j:
        if arr[i] <= p:
            i += 1
        if arr[j] >= p:
            j -= 1
        if i <= j:
            if arr[i] > p and arr[j] < p: 
                arr[i], arr[j] = arr[j], arr[i]
        else:
            arr[l], arr[j] =  arr[j], arr[l]
            break

    # arr[0], arr[j] = arr[j], arr[0]
    return j

t = int(input())
ans = ""

for i in range(1, t+1):
    n = int(input())
    nums = list(map(int, input().split()))
    
    quicksort(nums, 0, n-1)
    res = nums[n//2]
    ans += "#{} {}\n".format(i, res)

print(ans)