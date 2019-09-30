'''
1486. 장훈이의 높은 선반
'''

import sys
sys.stdin = open("SWEA/inputs/1486_in.txt", "r")

t = int(input())
ans = ""

for i in range(1, t+1):
    n, b = map(int, input().split())
    heights = [*map(int, input().split())]
    res = n * b

    for k in range(1, (1<<n)):
        s = 0
        for j in range(0, n):
            if k & (1<<j):
                s += heights[j]
                if s >= res:
                    break
        if b <= s < res: 
            res = s
        if res == b:
            break
    res -= b


    ans += "#{} {}\n".format(i, res)

print(ans)