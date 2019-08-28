'''
4047. 영준이의 카드 카운팅
'''

import sys
sys.stdin = open("SWEA/inputs/4047_in.txt", "r")

t = int(input())
ans = ""

for i in range(1, t+1):
    result = ""
    cards = list(input())
    cards_n = len(cards)//3
    card_cnt = [[1] * 14 for _ in range(4)]
    card_idx = {"S": 0, "D": 1, "H": 2, "C": 3}

    for _ in range(cards_n):
        shape = cards.pop(0)
        ten = cards.pop(0)
        one = cards.pop(0)
        cnt = int(ten + one)
        card_cnt[card_idx[shape]][cnt] -= 1

    flag = True
    for j in card_cnt:
        for k in range(1, 14):
            if j[k] not in [0, 1]:
                result = "ERROR"
                flag = False
        if flag:
            result += str(sum(j[1:])) + " "

    ans += "#{} {}\n".format(i, result)

print(ans)