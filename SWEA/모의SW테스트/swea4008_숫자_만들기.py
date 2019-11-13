'''
4008. [모의 SW 역량테스트] 숫자 만들기
'''

import sys
sys.stdin = open("SWEA/inputs/4008_in.txt", "r")

from itertools import permutations
from math import ceil

def cal(x, y, op):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    else:
        if x * y > 0:
            return x // y
        else:
            return ceil(x / y)

def dfs(v, op, ops, num_i):
    # if num_i == n:
    #     return

    if num_i > 0:
        global mx, mn
        v = cal(v, nums[num_i], op)
        
    if not ops:
        if v > mx:
            mx = v
        if v < mn:  
            mn = v
        return 
    set_ops = list(set(ops))

    for i in range(len(set_ops)):
        next_op = set_ops[i]
        tmp = ops[:]
        ops.pop(ops.index(next_op))
        dfs(v, next_op, ops, num_i+1)
        ops = tmp

    

ans = ""

for tc in range(1, int(input())+1):
    n = int(input())
    mn = 100000000
    mx = -100000000
    operators = list(map(int, input().split()))
    ops = []
    [ops.append('+') for _ in range(operators[0])]
    [ops.append('-') for _ in range(operators[1])]
    [ops.append('*') for _ in range(operators[2])]
    [ops.append('/') for _ in range(operators[3])]

    nums = list(map(int, input().split()))
    all_ops = set(list(permutations(ops)))

    for op in ops:
        v = 0
        for i in range(nums-1):
            


    # dfs(nums[0], None, ops, 0)
    

    # all_nums = list(permutations(nums))
    # res = all_nums
    res = mx - mn
    ans += "#{} {}\n".format(tc, res)

print(ans)