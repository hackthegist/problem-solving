'''
5186. [파이썬 S/W 문제해결 구현] 1일차 - 이진수2
'''

import sys
sys.stdin = open("SWEA/inputs/5186_in.txt", "r")

t = int(input())
ans = ""


for i in range(1, t+1):
    n = float(input())
    m = 1
    rs = ''

    while m < 14:
        r = n // (2 ** (-m))  
        n = n - r * (2 ** (-m))
        rs += str(int(r))
        if n == 0:
            break
        
        m += 1

    if m >= 13:
        res = 'overflow'
    else:
        res = rs

    ans += "#{} {}\n".format(i, res)

print(ans)