'''
1231. [S/W 문제해결 기본] 9일차 - 중위순회
'''

import sys
sys.stdin = open("SWEA/inputs/1231_in.txt", "r")

def left_child(root):
    return root*2

def right_child(root):
    return root*2 + 1

def in_order(root):
    global res
    
    if root <= n:
        in_order(left_child(root))
        res += tree[root][1]
        in_order(right_child(root))


ans = ""

for tc in range(1, 11):
    n = int(input())
    tree = [[0]*4] + [input().split() for _ in range(n)]
    res = ""

    in_order(1)

    ans += "#{} {}\n".format(tc, res)

print(ans)