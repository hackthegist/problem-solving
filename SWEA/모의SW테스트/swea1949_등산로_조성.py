'''
1949. [모의 SW 역량테스트] 등산로 조성
'''

import sys
sys.stdin = open("SWEA/inputs/1949_in.txt", "r")

def dfs(x ,y, d, chance):
    
    for mi, mj in [(1,0), (0,1), (-1,0), (0,-1)]:
        mi += x
        mj += y
        if not 0 <= mi < n:
            continue
        if not 0 <= mj < n:
            continue
        if hills[mi][mj] > -50:
            if hills[mi][mj] < hills[x][y]:
                tmp = hills[x][y]
                hills[x][y] = -50
                dfs(mi, mj, d+1, chance)
                hills[x][y] = tmp
            else:
                if chance and hills[mi][mj] - ks < hills[x][y]:
                    tmp = hills[x][y]
                    tmp1 = hills[mi][mj]
                    hills[mi][mj] = hills[mi][mj] - ks
                    hills[x][y] = -50
                    dfs(mi, mj, d+1, False)
                    hills[x][y] = tmp
                    hills[mi][mj] = tmp1

    global res
    res = res if res > d else d
    return


ans = ""


for tc in range(1, int(input())+1):
    n, k = map(int, input().split())
    hills = [list(map(int, input().split())) for _ in range(n)]
    res = 0

    mx = hills[0][0]
    mx_hills = []
    for i in range(n):
        for j in range(n):
            if hills[i][j] == mx:
                mx_hills.append((i,j))
            elif hills[i][j] > mx:
                mx_hills = []
                mx_hills.append((i,j))
                mx = hills[i][j]
    
    for mx_x, mx_y in mx_hills:
        for ks in range(k+1):
            dfs(mx_x, mx_y, 1, True)
                
    ans += "#{} {}\n".format(tc, res)

print(ans)



# for tc in range(1, int(input())+1):
#     n, k = map(int, input().split())
#     hills = [list(map(int, input().split())) for _ in range(n)]

#     mx = hills[0][0]
#     mx_hills = []
#     for i in range(n):
#         for j in range(n):
#             if hills[i][j] == mx:
#                 mx_hills.append((i,j))
#             elif hills[i][j] > mx:
#                 mx_hills = []
#                 mx_hills.append((i,j))
#                 mx = hills[i][j]
    
#     for mx_x, mx_y in mx_hills:
#         stack = []
#         stack.append([mx_x, mx_y, 0, -1, -1, False])

#         while stack:
#             x, y, d, prev_x, prev_y, use_chance = stack.pop()
#             d += 1
#             for mi, mj in [(1,0), (0,1), (-1,0), (0,-1)]:
#                 mi += x
#                 mj += y
#                 if not 0 <= mi < n:
#                     continue
#                 if not 0 <= mj < n:
#                     continue
#                 if mi == prev_x or mj == prev_y:
#                     continue
#                 if hills[mi][mj] < hills[x][y]:
#                     stack.append([mi, mj, d, x, y, False])
#                 else:
#                     if not use_chance and  hills[mi][mj] - k < hills[x][y]:
#                         stack2 = []
#                         stack2.append()
#                         while 
#                         stack.append([mi, mj, d, x, y, True])
#                         ch_x, ch_y = mi, mj
#                         hills[ch_x][ch_y] = hills[mi][mj] - k
#             else:
#                 res = res if res > d else d
            


#     ans += "#{} {}\n".format(tc, res)

# print(ans)