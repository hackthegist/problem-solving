'''
2383. [모의 SW 역량테스트] 점심 식사시간
'''

import sys
sys.stdin = open("SWEA/inputs/2383_in.txt", "r")

ans = ""

for tc in range(1, int(input())+1):
    n = int(input())
    room = [list(map(int, input().split())) for _ in range(n)]
    stairs = []    

    for i in range(n):
        for j in range(n):
            if room[i][j] > 1:
                stairs.append([i, j, room[i][j]])
           
    p_in_stairs = [[] for _ in range(len(stairs))]

    for i in range(n):
        for j in range(n):
            if room[i][j] == 1:
                mn = 1000
                mn_idx = None
                for k in range(len(stairs)):
                    dist = abs(i - stairs[k][0]) + abs(j - stairs[k][1])
                    if dist < mn:
                        mn_idx = k
                        mn = dist
                    elif dist == mn:
                        if stairs[mn_idx][2] > stairs[k][2]:
                            mn_idx = k
                p_in_stairs[mn_idx].append(mn)

    p_in_stairs = list(map(sorted, p_in_stairs))
    print(p_in_stairs)

    mx_t = 0
    for j in range(len(p_in_stairs)):
        waiting = p_in_stairs[j]
        t = 1 + waiting[0]
        down = []
        v = stairs[j][2]
        for i in range(len(waiting)):
            waiting[i] == t-1:
            down.append(v)

        while :
            for k in range(len(down)):
                down[k] -= 1
            while waiting and waiting[0] == 0:
                waiting.pop(0)
                down.append(v)

            



    mx_t = t if mx_t < t else mx_t    
print(mx_t)



        # if stair_time:
        #     stair_down = []
        #     mn = stair_time[0]
        #     t += mn
        #     if stair_time:
        #         while stair_time[0] == mn:
        #             stair_time.pop(0)
        #             stair_down.append(v)
        #             if not stair_time:
        #                 break
        #     while stair_down:
        #         if len(stair_down) >= 3:
        #             for i in range(3):
        #                 stair_down[i] -= 1
        #             if not stair_down:
        #                 break
        #         else:
        #             for i in range(len(stair_down)):
        #                 stair_down[i] -= 1
        #             if not stair_down:
        #                 break
        #         if stair_down:
        #             while stair_down[0] == 0:
        #                 stair_down.pop(0)
        #                 if not stair_down:
        #                     break
        #         t += 1
        #         if stair_time:
        #             while stair_time[0] == t-1:
        #                 stair_time.pop(0)
        #                 stair_down.append(v)
        #                 if not stair_time:
        #                     break
                

   
                    





    #     stair = p_in_stairs[j]
    #     if stair:
    #         t = 1 + stairs[j][2]
    #         while stair:
    #             mn = stair[0] 
    #             t += mn 
    #             if len(stair) >= 3:
    #                 for i in range(3):
    #                     stair[i] -= mn
    #                 while not stair[0]:
    #                     stair.pop(0)
    #                     if not stair:
    #                         break
    #             else: 
    #                 for i in range(len(stair)):
    #                     stair[i] -= mn
    #                 while not stair[0]:
    #                     stair.pop(0)
    #                     if not stair:
    #                         break
    #     mx_t = t if mx_t < t else mx_t 

    # print(mx_t)
  
    

    
    # ans += "#{} {}\n".format(tc, res)

print(ans)