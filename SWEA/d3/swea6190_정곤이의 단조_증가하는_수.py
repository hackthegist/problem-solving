'''
6190. 정곤이의 단조 증가하는 수
'''

import sys
sys.stdin = open("SWEA/inputs/6190_in.txt", "r")

t = int(input())
ans = ""

def is_inc(num):
    one = 10
    while num:
        if one >= num % 10:
            one = num % 10
            num //= 10
        else:
            return False
    return True

for tc in range(1, t+1):
    res = -1
    n = int(input())
    nums = list(map(int, input().split()))
    nums_mul = [nums[a] * nums[b] for a in range(0, n-1) for b in range(a+1, n)]

    for num in nums_mul:
        if is_inc(num):
            res = num if num > res else res

    ans += "#{} {}\n".format(tc, res)

print(ans)