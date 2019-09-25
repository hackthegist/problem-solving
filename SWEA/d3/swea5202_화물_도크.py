'''
5202. [파이썬 S/W 문제해결 구현] 3일차 - 화물 도크
'''

import sys
sys.stdin = open("SWEA/inputs/5202_in.txt", "r")

t = int(input())
ans = ""

for i in range(1, t+1):
    n = int(input())
    trucks = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[1], reverse=True)
    res = 0

    s_b, e_b = 25, 25
    for s, e in trucks:
        if e_b == e:
            s_b = s if s_b < s else s_b
        else:
            if e > s_b:
                if (e - s) < (e_b - s_b):
                    s_b, e_b = s, e
                else:
                    continue
            else:
                res += 1
                s_b, e_b = s, e


    ans += "#{} {}\n".format(i, res)

print(ans)