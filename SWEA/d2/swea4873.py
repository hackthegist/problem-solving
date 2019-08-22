'''
4873. [파이썬 S/W 문제해결 기본] 4일차 - 반복문자 지우기 
'''

import sys
sys.stdin = open("SWEA/inputs/4873_in.txt", "r")

t = int(input())
ans = ""

for i in range(1, t+1):
    sen = input()
    cnt = 0
    stack = []

    for ch in sen:
        if not stack:
            stack.append(ch)
        else:
            if stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
    while stack:
        cnt += 1
        stack.pop()

    ans += "#{} {}\n".format(i, cnt)

print(ans)
