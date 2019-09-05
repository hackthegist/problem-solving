'''
6109. 추억의 2048게임
'''

import sys
sys.stdin = open("SWEA/inputs/6109_in.txt", "r")

t = int(input())
ans = ""

def check(x, y):
    if not 0 <= x < n:
        return False
    if not 0 <= y < n:
        return False
    return True            

def up(s):
    for j in range(n):
        i = -1
        while i < n-1:
            i += 1
            x, y = i, j
            if nums[i][j]:
                x += 1
                y += 0
                if not check(x, y):
                    break
                while not nums[x][y]:
                    x += 1
                    y += 0
                    if not check(x, y):
                        break
                if check(x, y) and nums[x][y] == nums[i][j]:
                    nums[i][j], nums[x][y] = nums[i][j] * 2, 0

    for j in range(n):   
        i = -1
        while i < n-1:     
            i += 1
            if i > 0 and nums[i][j]:
                while not nums[i-1][j]:
                    nums[i][j], nums[i-1][j] = nums[i-1][j], nums[i][j]
                    i += -1
                    if not check(i-1,j):
                        break
                        
def rotate_r(nums, n):
    return [[nums[j][i] for j in range(n-1, -1, -1)] for i in range(n)]

def rotate_rr(nums, n):
    return [[nums[i][j] for j in range(n-1, -1, -1)] for i in range(n-1, -1, -1)]

def rotate_l(nums, n):
    return [[nums[j][i] for j in range(n)] for i in range(n-1, -1, -1)]



for tc in range(1, t+1):
    n, s = input().split()
    n = int(n)
    nums = [list(map(int, input().split())) for _ in range(n)]
    
    if s == "left":
        nums = rotate_r(nums, n)
        up(nums)
        nums = rotate_l(nums, n)
    elif s == "right":
        nums = rotate_l(nums, n)
        up(nums)
        nums = rotate_r(nums, n)
    elif s == "down":
        nums = rotate_rr(nums, n)
        up(nums)
        nums = rotate_rr(nums, n)
    else:
        up(nums)

    res = ""
    for i in range(n):
        for j in range(n):
            res += str(nums[i][j]) + " "
        res += "\n"

    ans += "#{}\n{}".format(tc, res)

print(ans)