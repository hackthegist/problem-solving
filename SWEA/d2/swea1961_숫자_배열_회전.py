'''
1961. 숫자 배열 회전
'''

import sys
sys.stdin = open("SWEA/inputs/1961_in.txt", "r")

def rotate(mts):
    return [[mts[j][i] for j in range(n-1, -1, -1)] for i in range(n)]



t = int(input())
ans = ""

for tc in range(1, t+1):
    res = ""
    n = int(input())
    mtx = [input().split() for _ in range(n)]

    ninety = rotate(mtx)
    one_eighty = rotate(ninety)
    two_seventy = rotate(one_eighty)

    for i in range(n):
        for mt in [ninety, one_eighty, two_seventy]:
            for j in range(n):
                res += mt[i][j]
            res += " "
        res += "\n" 

    ans += "#{}\n{}".format(tc, res)

print(ans)