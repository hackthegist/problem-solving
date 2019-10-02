'''
1247. [S/W 문제해결 응용] 3일차 - 최적 경로
'''

import sys
sys.stdin = open("SWEA/inputs/1247_in.txt", "r")

def go(visited, tot, cx, cy):
    visited = visited[:]
    global res

    if tot >= res:
        return
    if not sum(visited):
        for x in range(len(visited)):
            if visited[x]:
                cx, cy = custs[x] 
        tot += abs(cx-hx) + abs(cy-hy)
        res = tot if res > tot else res
        return 
    
    for i in range(len(visited)):
        if visited[i]:
            visited[i] = 0
            x, y = custs[i]
            go(visited, tot + (abs(cx - x)+abs(cy - y)), x, y)
            visited[i] = 1

t = int(input())
ans = ""

for tc in range(1, t+1):
    n = int(input())
    nums = [*map(int, input().split())]
    cx, cy, hx, hy = nums[0], nums[1], nums[2], nums[3]
    custs = sorted([(nums[l], nums[l+1]) for l in range(4, len(nums), 2)], 
            key=lambda x: abs(company[0]-x[0]) + abs(company[1]-x[1]))
    res = 200 * n

    go([1] * n, 0, cx, cy)
    
    ans += "#{} {}\n".format(tc, res)



print(ans)