'''
1493. 수의 새로운 연산
'''

import sys
sys.stdin = open("SWEA/inputs/1493_in.txt", "r")

def get_grid(num):
    m = num
    n = 1
    while m > 0:
        m -= n
        n += 1
    x = 1
    y = n-1
    diff = num - (sum(range(1, n-1)) + 1)
    for _ in range(diff):
        x += 1
        y += -1
    return (x, y)

def get_num(x, y):
    diff = x - 1
    start = sum(range(1, y + (x-1))) + 1
    return start + (x-1)

t = int(input())
ans = ""

for tc in range(1, t+1):
    p, q = map(int, input().split())

    x1, y1 = get_grid(p)
    x2, y2 = get_grid(q)
    x_new = x1 + x2
    y_new = y1 + y2
    print(x_new, y_new)
    res = get_num(x_new, y_new)

    ans += "#{} {}\n".format(tc, res)

print(ans)