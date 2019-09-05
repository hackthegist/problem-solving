'''
1224. [S/W 문제해결 기본] 6일차 - 계산기3
'''

import sys
sys.stdin = open("SWEA/inputs/1224_in.txt", "r")

t = 10
ans = ""

for i in range(1, t+1):
    n = int(input())
    nums = input()
    stack = []
    digit = []

    for ch in nums:
        if ch.isdigit():
            digit.append(ch)
        elif ch in ["+", "-"]:
            while stack[-1] in ["*", "/"]:
                digit.append(stack.pop())
            stack.append(ch)
        elif ch == ")":
            while True:
                pop_ = stack.pop()
                if pop_ == "(":
                    break
                else:
                    digit.append(pop_)
        else:
            stack.append(ch)

    digit = "".join(digit)
    stack = []
    for ch in digit:
        if ch.isdigit():
            stack.append(int(ch))
        else:
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
            stack.append(v)
    else:
        result = stack.pop()

    ans += "#{} {}\n".format(i, result)

print(ans)
