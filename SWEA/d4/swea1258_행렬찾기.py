'''
1258. [S/W 문제해결 응용] 7일차 - 행렬찾기
'''

import sys
sys.stdin = open("SWEA/inputs/1258_in.txt", "r")

t = int(input())
ans = ""

for tc in range(1, t+1):
    n = int(input())
    nums = [input().split() for _ in range(n)]
    mts = []

    for i in range(n):
        for j in range(n):
            r_cnt = c_cnt = 0
            if nums[i][j] != "0":
                if (i == 0 and j == 0) or (i == 0 and nums[i][j-1] == "0") or (nums[i-1][j] == "0" and j == 0) or (nums[i-1][j] == "0" and nums[i][j-1] == "0"):
                    x, y = i, j
                    while nums[x][y] != "0":
                         c_cnt += 1
                         y += 1
                         if y > n-1:
                             break
                    x, y = i, j
                    while nums[x][y] != "0":
                         r_cnt += 1
                         x += 1
                         if x > n-1:
                            break
                    mts.append((r_cnt, c_cnt))
    for l in range(len(mts)-1):
        for m in range(l+1, len(mts)):
            if mts[l][0] * mts[l][1] > mts[m][0] * mts[m][1]:
                mts[l], mts[m] = mts[m], mts[l]
            elif mts[l][0] * mts[l][1] == mts[m][0] * mts[m][1]:
                if mts[l][0] > mts[m][0]:
                    mts[l], mts[m] = mts[m], mts[l]

    res = "{} ".format(len(mts))
    for mt in mts:
        res += "{} {} ".format(mt[0], mt[1])

    ans += "#{} {}\n".format(tc, res)

print(ans)