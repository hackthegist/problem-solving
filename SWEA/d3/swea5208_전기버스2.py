'''
5208. [파이썬 S/W 문제해결 구현] 5일차 - 전기버스2
'''

import sys
sys.stdin = open("SWEA/inputs/5208_in.txt", "r")

def bus(s, b, p):
    global res

    if p >= res:
        return
    if b >= nums[0] - s:
        res = p if res > p else res
        return 

    for i in range(1, nums[s]+1):
        if s + i >= nums[0]:
            res = p if res > p else res
            return 
        else:
            bus(s+i, nums[s+i], p+1)


t = int(input())
ans = ""

for i in range(1, t+1):
    nums = [*map(int, input().split())]
    res = nums[0]

    bus(1, nums[1], 0)
    ans += "#{} {}\n".format(i, res)

print(ans)