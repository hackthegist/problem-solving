'''
4866. [파이썬 S/W 문제해결 기본] 4일차 - 괄호검사
'''

import sys
sys.stdin = open("SWEA/inputs/4866_in.txt", "r")


def p_check(sen):
    open_p = "{("
    close_p = ")}"
    stack = []

    for ch in sen:
        if ch in open_p:
            stack.append(ch)

        if ch in close_p:
            if not stack:
                return 0
            else:
                pop_n = stack.pop(-1)
                if ch == "}" and pop_n != "{":
                    return 0
                if ch == ")" and pop_n != "(":
                    return 0
    if not stack:
        return 1
    else:
        return 0


t = int(input())
ans = ""

for i in range(1, t+1):
    sen = input()

    ans += "#{} {}\n".format(i, p_check(sen))

print(ans)
