'''
5356. 의석이의 세로로 말해요
'''

import sys
sys.stdin = open("SWEA/inputs/5356_in.txt", "r")

t = int(input())
ans = ""

for tc in range(1, t+1):
    res = ""
    strs = [list(input()) for _ in range(5)]

    mx = 0
    for s in strs:
        mx = len(s) if len(s) > mx else mx

    for i in range(mx):
        for j in range(5):
            if i > len(strs[j])-1:
                continue
            res += strs[j][i]

    ans += "#{} {}\n".format(tc, res)

print(ans)