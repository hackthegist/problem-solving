'''
5203. [파이썬 S/W 문제해결 구현] 3일차 - 베이비진 게임
'''

import sys
sys.stdin = open("SWEA/inputs/5203_in.txt", "r")

def is_run(cards):
    cards = sorted(cards)
    num, cnt = cards[0], 1
    for card in cards[1:]:
        if card != num:
            num = card
            cnt = 1
        else:
            cnt += 1
        if cnt == 3:
            return True
    return False

def is_triplet(cards):
    cards = sorted(cards)
    num, cnt = cards[0], 1
    for card in cards[1:]:
        if card != num:
            if card == num + 1:
                num = card
                cnt += 1
            else:
                num = card
                cnt = 1
        else:
            continue
        if cnt == 3:
            return True
    return False

t = int(input())
ans = ""

for i in range(1, t+1):
    cards = list(map(int, input().split()))
    cards_a = []
    cards_b = []
    res = 0

    for j in range(len(cards)):
        if j < 4:
            if j % 2 == 0:
                cards_a.append(cards[j])
            else:
                cards_b.append(cards[j])
        else:
            if j % 2 == 0:
                cards_a.append(cards[j])
                if is_run(cards_a) or is_triplet(cards_a):
                    res = 1
                    break
            else:
                cards_b.append(cards[j])
                if is_run(cards_b) or is_triplet(cards_b):
                    res = 2
                    break
    


    ans += "#{} {}\n".format(i, res)

print(ans)