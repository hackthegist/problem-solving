'''
5185. [파이썬 S/W 문제해결 구현] 1일차 - 이진수
'''

import sys
sys.stdin = open("SWEA/inputs/5185_in.txt", "r")

t = int(input())
ans = ""

for i in range(1, t+1):
    n, st = input().split()
    int_ = int(st, 16)
    bin_ = bin(int_)[2:]
    bin_ = ('0' * (4*int(n) - len(bin_))) + bin_
    
    res = bin_

    ans += "#{} {}\n".format(i, res)

print(ans)