'''
1974. 스도쿠 검증
'''

import sys
sys.stdin = open("SWEA/inputs/1974_in.txt", "r")

def check(s):
    for i in range(9):
        if sum(s[i]) != 45:
            return 0
    
    for i in range(9):
        sum_ = 0
        for j in range(9):
            sum_ += s[j][i]
        if sum_ != 45:
            return 0

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sum_ = 0
            for k in range(i, i+3):
                for l in range(j, j+3):
                    sum_ += s[k][l]
            if sum_ != 45:
                return 0
    return 1


t = int(input())
ans = ""

for tc in range(1, t+1):
    sdoku = [list(map(int, input().split())) for _ in range(9)]
    res = check(sdoku)

    ans += "#{} {}\n".format(tc, res)

print(ans)