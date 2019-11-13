'''
2117. [모의 SW 역량테스트] 홈 방범 서비스
'''

import sys
sys.stdin = open("SWEA/inputs/2117_in.txt", "r")

def get_house():
    res = []
    for i in range(n):
        for j in range(n):
            if vill[i][j] == 1:
                res.append((i,j))
    return res

def get_points_in_dist(houses, k):
    res = []
    for i in range(n):
        for j in range(n):
            for x, y in houses:
                if abs(i - x) + abs(j - y) <= k:
                    res.append((i,j))
    return res

def get_max_profit(points):
    res = {}
    for point in points:
        if point in res.keys():
            res[point] += 1
        else:
            res[point] = 1
    return max(res.values()) * m



ans = ""

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    vill = [list(map(int, input().split())) for _ in range(n)]

    houses = get_house()

    for i in range(n+1, 0, -1):
        service = (i ** 2) + (i-1) ** 2
        fee = get_max_profit(get_points_in_dist(houses, i-1))
        if fee - service >= 0:
            max_house = fee // m
            break 

    res = max_house
    ans += "#{} {}\n".format(tc, res)

print(ans)