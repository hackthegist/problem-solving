'''
1259. [S/W 문제해결 응용] 7일차 - 금속막대
'''

import sys
sys.stdin = open("inputs/1259_in.txt", "r")


# def concat(x_li, y_li):
#     return x_li + y_li if x_li[-1] == y_li[0] else y_li + x_li


# def can_concat(x_li, y_li):
#     x_0, x_l = x_li[0], x_li[-1]
#     y_0, y_l = y_li[0], y_li[-1]
#     return x_l == y_0 or x_0 == y_l

def can_concat(x, y):
    xl, xr = x
    yl, yr = y
    if xl == yr:
        return "right"
    elif xr == yl:
        return "left"
    else:
        return False
    # return xl == yr or xr == yl


t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    screws = list(zip(nums[::2], nums[1::2]))
    # screws = [[nums[x], nums[x+1]] for x in range(len(nums)//2)]

    for j in range(n-1):
        for k in range(j, n):
            if can_concat(screws[j], screws[k]) == "left":
                screws[j+1], screws[k] = screws[k], screws[j+1]
                break

    result = screws
    print("#{} {}".format(i+1, result))
