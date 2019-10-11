'''
1232. [S/W 문제해결 기본] 9일차 - 사칙연산
'''

import sys
sys.stdin = open("SWEA/inputs/1232_in.txt", "r")

def calc(shape, a, b):
    a, b = float(a), float(b)
    if shape == "+":
        return str(a + b)
    elif shape == "-":
        return str(a - b)
    elif shape == "*":
        return str(a * b)
    else:
        return str(a / b)

def inorder(root):

    if tree[root][1].isdigit():
        return tree[root][1]
    else:
        return calc(tree[root][1], inorder(int(tree[root][2])), inorder(int(tree[root][3])))

ans = ""

for tc in range(1, 10+1):
    n = int(input())
    tree = [[0]*4] + [list(input().split()) for _ in range(n)]
    res = round(float(inorder(1)))
    # tree[1][1] = calc(tree[1][1], tree[1*2][1], tree[1*2+1][1])
    # res = int(float(tree[1][1]))
    ans += "#{} {}\n".format(tc, res)

print(ans)