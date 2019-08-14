'''
1259. [S/W 문제해결 응용] 7일차 - 금속막대
'''

import sys
sys.stdin = open("../inputs/1259_in.txt", "r")


t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    # screws = list(zip(nums[::2], nums[1::2]))
    screws = [[nums[x], nums[x+1]] for x in range(0, len(nums), 2)]

    for k in range(n):
        if screws[k][0] not in nums[1::2]:
            result = [screws[k]]

    while len(result) != len(screws):
        for j in range(n):
            if result[-1][-1] == screws[j][0]:
                result = result + [screws[j]]

    print("#{}".format(i+1), end=" ")
    for l in range(len(result)):
        for m in range(len(result[l])):
            print(result[l][m], end=" ")
    print()
