'''
1861. 정사각형 방
'''

import sys
sys.stdin = open("SWEA/inputs/1861_in.txt", "r")

ans = ""

for tc in range(1, int(input())+1):
    n = int(input())
    nums = [[*map(int, input().split())] for _ in range(n)]
    moves = [(1,0), (-1,0), (0,1), (0,-1)]
    v, dist = 1, 1
    visited = [0] * (n**2 + 1)

    for i in range(n):
        for j in range(n):
            if not visited[nums[i][j]]:
                i_b, j_b, s = i, j, 1
                # visited[nums[i][j]] = 1

                while True:
                    for x, y in moves:
                        x += i
                        y += j
                        if 0 <= x < n and 0 <= y <n:
                            if nums[x][y] == nums[i][j] + 1:
                                i, j = x, y
                                s += 1
                                break
                    else:
                        break
                visited[nums[i_b][j_b]:nums[i][j]] = [1] * (nums[i][j] - nums[i_b][j_b])       
                if s > dist:
                    v, dist = nums[i_b][j_b], s
                elif s == dist:
                    if nums[i_b][j_b] < v:
                        v = nums[i_b][j_b]
                
                          
    ans += "#{} {} {}\n".format(tc, v, dist)

print(ans)