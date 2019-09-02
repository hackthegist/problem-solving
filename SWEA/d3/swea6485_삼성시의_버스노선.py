'''
6485. 삼성시의 버스 노선
'''

import sys
sys.stdin = open("SWEA/inputs/6485_in.txt", "r")

t = int(input())
ans = ""

for tc in range(1, t+1):
    n = int(input())
    stations = [0] * 5001
    mx = 0

    for i in range(n):
        a, b = map(int, input().split())
        mx = b if b > mx else mx

        for j in range(a, b+1):
            stations[j] += 1

    p = int(input())
    res = ""

    for _ in range(p):
        res += str(stations[int(input())]) + " "

    ans += "#{} {}\n".format(tc, res)

print(ans)