'''
5249. [파이썬 S/W 문제해결 구현] 7일차 - 최소 신장 트리
'''

import sys
sys.stdin = open("SWEA/inputs/5249_in.txt", "r")

ans = ""

for tc in range(1, int(input())+1):
    v, e = map(int, input().split())
    vertex = [-1] * (v+1)
    edges = sorted([tuple(map(int, input().split())) for _ in range(e)], key=lambda x: x[2])
    res = 0
    edge = 0

    for a, b, w in edges:
        if not vertex[a] >= 0: 
            if not vertex[b] >= 0:
                vertex[a] = vertex[b] = a
                res += w
                edge += 1
            else:
                vertex[a] = vertex[b]
                res += w
                edge += 1
        else:
            if not vertex[b] >= 0:
                vertex[b] = vertex[a]
                res += w
                edge += 1
            else:
                if not vertex[b] == vertex[a]:
                    to = vertex[b]
                    for j in range(len(vertex)):
                        if vertex[j] == to:
                            vertex[j] = vertex[a]
                    res += w
                    edge += 1
        
        if edge == v:
            break
    
    ans += "#{} {}\n".format(tc, res)

print(ans)