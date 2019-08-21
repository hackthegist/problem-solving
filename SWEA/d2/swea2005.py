'''
2005. 파스칼의 삼각형
'''

import sys
sys.stdin = open("SWEA/inputs/2005_in.txt", "r")

t = int(input())
ans = ""

for i in range(1, t+1):
    n = int(input())
    nums = list(map(int, input().split()))

    ans += "#{} {}\n".format(i, result)

print(ans)
