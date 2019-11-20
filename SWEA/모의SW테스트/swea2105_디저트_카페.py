'''
2105. [모의 SW 역량테스트] 디저트 카페
'''

import sys
sys.stdin = open("SWEA/inputs/2105_in.txt", "r")

# def tour(lst):
#     global tour_dict
#     res = []
#     for l in lst:
#         n_l = l[:]
#         length = len(l)
#         i, j = l[length-1]
#         dx, dy = move[length-1]

#         i += dx
#         j += dy
#         if 1 < length <= 4:
#             while 0 <= i < n and 0 <= j < n:
#                 if cafes[i][j] in tour_dict[l[length-1]]:
#                     break
#                 n_l.append((i,j))
#                 n_lst[0].append(cafes[i][j])
#                 res.append(n_lst)
#                 i += dx
#                 j += dy
#                 n_lst = lst[:]

#             if res:
#                 return res
#     else:
#         if i == lst[0][0] and j == lst[0][1]:
#             return len(visited)


def start():
    global visited
    for i in range(n-2):
        for j in range(1, n-1):\
            yield (i,j)

ans = ""

for tc in range(1, int(input())+1):
    n = int(input())
    cafes = [list(map(int, input().split())) for _ in range(n)]
    move = [(1,-1), (1,1), (-1,1), (-1,-1)]
    tour_dict = {}
    mx = 0
    
    
    for s1 in start():
        tour_dict[s1] = [cafes[s1[0]][s1[1]]]

    print(tour_dict)
    # for s2 in step2:
    #     if s2:
    #         step3 += tour(s2)
    # print(step3)
            # for s3 in step3:
            #     print(s3)
            #     print(s3)




        # step2 = tour(s1)

        # step3 = []
        # for s2 in step2:
        #     step3 += tour(s2)
        # print(step2)
        
        # if step2:
        #     for s2 in step2:
        #         if s2:
        #             step3 = tour(s2)
        #             if step3:
        #                 for s3 in step3:
        #                     if s3:
        #                         fin = tour(s3)
        #                         if fin:
        #                             for f in fin:
        #                                 if f:
        #                                     a = tour(f)
        #                                     if a:
        #                                         mx = a if mx < a else mx
                                     
                                
    res = mx
    ans += "#{} {}\n".format(tc, res)

print(ans)