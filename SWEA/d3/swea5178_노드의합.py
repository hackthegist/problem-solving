'''
5178. [파이썬 S/W 문제해결 기본] 8일차 - 노드의 합
'''

import sys
sys.stdin = open("SWEA/inputs/5178_in.txt", "r")

ans = ""

for tc in range(1, int(input())+1):
    n, m, l = map(int, input().split())
    
    tree = [0] * (n+1)
    if n % 2 == 0:
        tree.append(0)
    for node, value in [map(int, input().split()) for _ in range(m)]:
        tree[node] = value
    for i in range(len(tree)-2, 1, -2):
        tree[i//2] = (tree[i] + tree[i+1])
    

    res = tree[l]
    ans += "#{} {}\n".format(tc, res)

print(ans)