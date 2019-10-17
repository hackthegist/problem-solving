'''
5248. [파이썬 S/W 문제해결 구현] 6일차 - 그룹 나누기
'''

import sys
sys.stdin = open("SWEA/inputs/5248_in.txt", "r")

ans = ""

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    nodes = list(map(int, input().split()))
    reprs = [0] * (n+1)

    for a, b in [(nodes[x], nodes[x+1]) for x in range(0, len(nodes), 2)]:
        if not reprs[a]: 
            if not reprs[b]:
                reprs[a] = reprs[b] = a
            else:
                reprs[a] = reprs[b]
        else:
            if not reprs[b]:
                reprs[b] = reprs[a]
            else:
                to = reprs[b]
                for j in range(len(reprs)):
                    if reprs[j] == to:
                        reprs[j] = reprs[a]
    for i in range(n+1):
        if not reprs[i]:
            reprs[i] = i
    groups = set(reprs[1:])
    res = len(groups)
    ans += "#{} {}\n".format(tc, res)

print(ans)