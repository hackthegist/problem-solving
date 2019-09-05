'''
4880. [파이썬 S/W 문제해결 기본] 5일차 - 토너먼트 카드게임
'''

import sys
sys.stdin = open("SWEA/inputs/4880_in.txt", "r")


def card_game(arr):
    if len(arr) == 2:
        lhs, rhs = arr[0], arr[1]
        if lhs - rhs == 0:
            win = lhs
        elif lhs - rhs in [-1, 2]:
            win = rhs
        else:
            win = lhs
        return win
    else:
        card_game(arr[:len(arr)//2])
        card_game(arr[len(arr)//2+1:])


t = int(input())
ans = ""

for i in range(1, t+1):
    n = int(input())
    nums = list(map(int, input().split()))
    result = def
    ans += "#{} {}\n".format(i, result)

print(ans)
