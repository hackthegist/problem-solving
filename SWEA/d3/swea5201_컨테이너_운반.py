'''
5201. [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반
'''

import sys
sys.stdin = open("SWEA/inputs/5201_in.txt", "r")

def get_mx(limit):
    mx = 0
    for bag in bags:
        if mx < bag <= limit:
            mx = bag
    return bags.pop(bags.index(mx)) if mx else 0
        

t = int(input())
ans = ""

for i in range(1, t+1):
    n, m = map(int, input().split())
    bags = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    res = 0

    for truck in trucks:
        res += get_mx(truck)

    ans += "#{} {}\n".format(i, res)

print(ans)