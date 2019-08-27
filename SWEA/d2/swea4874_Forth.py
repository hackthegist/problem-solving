'''
4874. [파이썬 S/W 문제해결 기본] 5일차 - Forth
'''

import sys
sys.stdin = open("SWEA/inputs/4874_in.txt", "r")

t = int(input())
ans = ""

for i in range(1, t+1):
    nums = input().split()
    stack = []
    result = None

    for ch in nums[:-1]:
        if ch.isdigit():
            stack.append(int(ch))
        else:
            if len(stack) < 2:
                result = "error"
                break
            rhs = stack.pop()
            lhs = stack.pop()
            if ch == "+":
                v = lhs + rhs
            elif ch == "-":
                v = lhs - rhs
            elif ch == "*":
                v = lhs * rhs
            elif ch == "/":
                v = lhs // rhs
            else:
                result = "error"
                break
            stack.append(v)
    else:
        if len(stack) == 1:
            result = stack.pop() 
        else:
            result = "error"
    ans += "#{} {}\n".format(i, result)

print(ans)
