'''
5174. [파이썬 S/W 문제해결 기본] 8일차 - subtree
'''

import sys
sys.stdin = open("SWEA/inputs/5174_in.txt", "r")

ans = ""

for tc in range(1, int(input())+1):
    e, n = map(int, input().split())
    nodes = [ [0] * (e+2) for _ in range(2) ]
    rels = list(map(int, input().split())) 

    for i in range(0, e*2, 2):
        if not nodes[0][rels[i]]:
            nodes[0][rels[i]] = rels[i+1]
        else:
            nodes[1][rels[i]] = rels[i+1]
    res = 0

    stack = [n]
    while stack:
        pp = stack.pop()
        res += 1
        if nodes[0][pp]:
            stack.append(nodes[0][pp])
        if nodes[1][pp]:
            stack.append(nodes[1][pp])

    ans += "#{} {}\n".format(tc, res)

print(ans)