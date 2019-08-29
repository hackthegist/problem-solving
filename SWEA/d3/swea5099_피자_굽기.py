'''
5099. [파이썬 S/W 문제해결 기본] 6일차 - 피자 굽기
'''

import sys
sys.stdin = open("SWEA/inputs/5099_in.txt", "r")

t = int(input())
ans = ""

for tc in range(1, t+1):
    n, m = map(int, input().split())
    cheezes = list(map(int, input().split()))
    pizzas = [[i+1, cheezes[i]] for i in range(m)]
    # cheeses = list(map(int, input().split()))
    # pizzas = [1] * (m+1)
    oven = []

    for _ in range(n):
            oven.append(pizzas.pop(0))

    pops = 0
    front = 0
    while True:
        if oven[front]:
            if oven[front][1] == 0:
                if pizzas:
                    oven[front] = pizzas.pop(0)
                    oven[front][1] //= 2
                    pops += 1
                else:
                    oven[front] = None
                    pops += 1
            else:
                oven[front][1] //= 2
        front = (front + 1) % n
        if pops == m-1:
            break

    for i in oven:
        if i:
            res = i[0]

    ans += "#{} {}\n".format(tc, res)

print(ans)