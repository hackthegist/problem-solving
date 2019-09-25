'''
5189. [파이썬 S/W 문제해결 구현] 2일차 - 전자카트
'''

import sys
sys.stdin = open("SWEA/inputs/5189_in.txt", "r")

def min_b(x, to, s):
    global res

    if s > res:
        return
        
    to = to[:]
    to.pop(to.index(x))
    if to:
        for i in to:
            s += nums[x][i]
            min_b(i, to, s)
            s -= nums[x][i]
    else:
        s += nums[x][0]
        res = s if res > s else res

t = int(input())
ans = ""

for i in range(1, t+1):
    n = int(input())
    nums = [list(map(int, input().split())) for _ in range(n)]
    res = 100 * n * n
    to = list(range(n))
    min_b(0, to, 0)


    ans += "#{} {}\n".format(i, res)

print(ans)