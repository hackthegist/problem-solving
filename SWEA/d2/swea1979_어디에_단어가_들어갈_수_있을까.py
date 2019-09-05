'''
1979. 어디에 단어가 들어갈 수 있을까
'''

import sys
sys.stdin = open("SWEA/inputs/1979_in.txt", "r")

def is_fit(ones, k):
    return ones == [1] * k

t = int(input())
ans = ""

for tc in range(1, t+1):
    n, k = map(int, input().split())
    nums = [list(map(int, input().split())) for _ in range(n)]
    rotated_nums = [[nums[j][i] for j in range(n)] for i in range(n-1, -1, -1)]
    res = 0

    for num in [nums, rotated_nums]:
        for i in range(n):
            for j in range(n-k+1):
                if 0 < j < n-k:
                    if is_fit(num[i][j:j+k], k) and not is_fit(num[i][j+1:j+k+1], k) and not is_fit(num[i][j-1:j+k-1], k):
                        res += 1
                        
                elif j == 0:
                    if is_fit(num[i][j:j+k], k) and not is_fit(num[i][j+1:j+k+1], k):
                        res += 1
                elif j == n-k:
                    if is_fit(num[i][j:j+k], k) and not is_fit(num[i][j-1:j+k-1], k):
                        res += 1

    ans += "#{} {}\n".format(tc, res)

print(ans)