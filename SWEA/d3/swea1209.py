'''
1209. [S/W 문제해결 기본] 2일차 - Sum
'''

# import sys
# sys.stdin = open("../inputs/1209.txt", "r")

# from scratch


def get_sum(nums):
    result = 0
    for num in nums:
        result += num
    return result


def get_max(nums):
    mx = 0
    for num in nums:
        mx = num if mx < num else mx
    return mx


for i in range(10):

    t = int(input())
    mat = [list(map(int, input().split())) for _ in range(100)]

    r_mx = get_max([get_sum(row) for row in mat])
    c_mx = get_max([get_sum([mat[r][c] for r in range(100)])
                    for c in range(100)])
    l_cross = get_sum([mat[x][x] for x in range(100)])
    r_cross = get_sum([mat[y][99-y] for y in range(100)])

    sum_list = []
    sum_list += [r_mx, c_mx, l_cross, r_cross]

    print("#{} {}".format(t, get_max(sum_list)))


# use built-in
for i in range(10):

    t = int(input())
    mat = [list(map(int, input().split())) for _ in range(100)]

    r_mx = max([sum(row) for row in mat])
    c_mx = max([sum([mat[r][c] for r in range(100)])
                for c in range(100)])
    l_cross = sum([mat[x][x] for x in range(100)])
    r_cross = sum([mat[y][99-y] for y in range(100)])

    sum_list = []
    sum_list += [r_mx, c_mx, l_cross, r_cross]

    print("#{} {}".format(t, max(sum_list)))
