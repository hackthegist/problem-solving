'''
5207. [파이썬 S/W 문제해결 구현] 4일차 - 이진 탐색
'''

import sys
sys.stdin = open("SWEA/inputs/5207_in.txt", "r")

def binary_search(a, b):
    i, j = 0, len(a)-1
    m = (i + j) // 2  
    w = 0
    v = 1 if a[m] < b else -1

    while i <= j:
        m = (i + j) // 2   

        if w != v and w != 0:
            return False

        if i < j:
            if a[m] == b:
                return True
            elif b > a[m]:
                i, j = m+1, j
                w += 1
            else:
                i, j = i, m-1
                w -= 1
    
        else:
            if a[m] == b:
                return True
            else: 
                return False


t = int(input())
ans = ""

for i in range(1, t+1):
    n, m = map(int, input().split())
    a = sorted([*map(int, input().split())])
    b = [*map(int, input().split())]
    res = 0

    for elem in b:
        if binary_search(a, elem):
            res += 1 

    ans += "#{} {}\n".format(i, res)

print(ans)