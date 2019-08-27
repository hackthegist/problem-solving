'''
4881. [파이썬 S/W 문제해결 기본] 5일차 - 배열 최소 합
'''

import sys
sys.stdin = open("SWEA/inputs/4881_in.txt", "r")

def checknode(x, y):
    
    for j in range(1, n):



t = int(input())
ans = ""

for i in range(1, t+1):
    n = int(input())
    nums = [list(map(int, input().split())) for _ in range(n)]

    ans += "#{} {}\n".format(i, result)

print(ans)