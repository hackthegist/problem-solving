'''
2805. 농작물 수확하기
'''

import sys
sys.stdin = open("SWEA/inputs/2805_in.txt", "r")

t = int(input())
ans = ""

for tc in range(1, t+1):
    res = 0
    n = int(input())
    values = [list(input()) for _ in range(n)]

    for i in range(n//2):
        for j in range(n//2-i, n//2+i+1):
            res += int(values[i][j])

    for i in range(n//2, n):
        for j in range(n//2-(n-i-1), n//2+(n-i)):
            res += int(values[i][j])

    ans += "#{} {}\n".format(tc, res)

print(ans)