'''
1220. [S/W 문제해결 기본] 5일차 - Magnetic
'''

import sys
sys.stdin = open("SWEA/inputs/1220_in.txt", "r")

t = 10
ans = ""

for i in range(1, t+1):
    n = int(input())
    tbl = [input().split() for _ in range(n)]
    cnt = 0

    for j in range(n):
        stack = []
        flag = False
        for k in range(n):
            if tbl[k][j] == "1":
                if flag == True:
                    cnt += 1
                    flag = False
                    stack = []
                stack.append("1")
            if tbl[k][j] == "2":
                if not stack:
                    continue
                else:
                    stack.pop()
                    flag = True
                    if not stack and flag:
                        cnt += 1
                        flag = False
            if k == n-1 and flag:
                cnt += 1
    ans += "#{} {}\n".format(i, cnt)

print(ans)

# t = 10
# for i in range(1, t+1):
#     n = int(input())
#     tbl = [input().split() for _ in range(n)]
#     cnt = 0

#     for x in range(n):
#         flag = 0
#         for y in range(n):
#             if tbl[y][x]:
#                 if tbl[y][x] == '1':
#                     flag = 1
#                 elif tbl[y][x] == '2':
#                     if flag == 1:
#                         cnt += 1
#                     flag = 2
#         print("#{} {} {}".format(i, x, cnt))

#     print('#{} {}'.format(i, cnt))
