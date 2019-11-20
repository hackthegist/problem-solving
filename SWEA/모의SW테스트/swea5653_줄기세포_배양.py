'''
5653. [모의 SW 역량테스트] 줄기세포배양
'''

import sys
sys.stdin = open("SWEA/inputs/5653_in.txt", "r")

ans = ""

for tc in range(1, int(input())+1):
    n, m, k = map(int, input().split())
    cells = [list(map(int, input().split())) for _ in range(n)]

    ans += "#{} {}\n".format(tc, res)

print(ans)