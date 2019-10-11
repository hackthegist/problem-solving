'''
5177. [파이썬 S/W 문제해결 기본] 8일차 - 이진 힙
'''

import sys
sys.stdin = open("SWEA/inputs/5177_in.txt", "r")

ans = ""

for tc in range(1, int(input())+1):
    n = int(input())
    nums = list(map(int, input().split()))
    tree = [0] * (n+1)

    for num in nums:
        i = 1
        while tree[i]:
            i += 1
        tree[i] = num
        while i > 1:
            if tree[i] < tree[i//2]:
                tree[i], tree[i//2] = tree[i//2], tree[i]
                i //= 2
            else:
                break
    res = 0
    j = n // 2
    while j > 0:
        res += tree[j]
        j //= 2

    ans += "#{} {}\n".format(tc, res)
print(ans)