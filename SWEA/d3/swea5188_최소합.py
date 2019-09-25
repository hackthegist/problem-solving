'''
5188. [파이썬 S/W 문제해결 구현] 2일차 - 최소합
'''

import sys
sys.stdin = open("SWEA/inputs/5188_in.txt", "r")

t = int(input())
ans = ""

def min_sum(x, y, s):
    global res
    if res <= s:
        return 
        
    s += nums[x][y]
    if x == n-1 and y == n-1:
        res = s if s < res else res
        return
    
    if x == n-1:
        move = [(0, 1)]
    elif y == n-1:
        move = [(1, 0)]
    else:
        move = [(1, 0), (0, 1)]

    for i, j in move:
        min_sum(x + i, y + j, s)
    

for i in range(1, t+1):
    n = int(input())
    nums = [list(map(int, input().split())) for _ in range(n)]
    res = 10 * 13 * 13

    min_sum(0, 0, 0)

    ans += "#{} {}\n".format(i, res)

print(ans)