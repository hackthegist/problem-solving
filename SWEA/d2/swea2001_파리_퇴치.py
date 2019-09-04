'''
2001. 파리 퇴치
'''

import sys
sys.stdin = open("SWEA/inputs/2001_in.txt", "r")

t = int(input())
ans = ""

for tc in range(1, t+1):
    res = 0
    n, m = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n-m+1):
        for j in range(n-m+1):
            sum_ = 0
            for k in range(i, i+m):
                for l in range(j, j+m):
                    sum_ += flies[k][l]
            res = sum_ if sum_ > res else res

    ans += "#{} {}\n".format(tc, res)

print(ans)