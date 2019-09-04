'''
2005. 파스칼의 삼각형
'''

import sys
sys.stdin = open("SWEA/inputs/2005_in.txt", "r")

t = int(input())
ans = ""

for tc in range(1, t+1):
    res = ""
    n = int(input())

    for i in range(n):
        if i == 0:
            floor = [0, 1, 0]   
            res += str(floor[1])
        else:
            floor = [0] + [floor[x] + floor[x+1] for x in range(len(floor)-1)] + [0]
            for num in floor[1:-1]:
                res += str(num) + " "
        res += "\n"

    ans += "#{}\n{}".format(tc, res)

print(ans)
