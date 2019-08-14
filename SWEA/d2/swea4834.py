'''
4834. [파이썬 S/W 문제해결 기본] 1일차 - 숫자 카드
'''

# 1. using counting list
t = int(input())
for i in range(t):
    card_count = int(input())
    card_list = [int(x) for x in input()]
    count_list = [0] * 10
    mx = 0

    # 1.1 value access
    for num in card_list:
        count_list[num] += 1
        mx = count_list[num] if mx < count_list[num] else mx
    for j in range(9, -1, -1):
        if count_list[j] == mx:
            break
    print("#{} {} {}".format(i+1, j, count_list[j]))

    # 1.2 index access


# 2. using dict
t = int(input())
for i in range(t):
    cards_len = int(input())
    cards = input()
    each_card_len_dict = {}

    for card in cards:
        if card in each_card_len_dict.keys():
            each_card_len_dict[card] += 1
        else:
            each_card_len_dict[card] = 1
    max_len = max(each_card_len_dict.values())
    max_len_card = 0

    for k, v in each_card_len_dict.items():
        if v == max_len:
            if int(k) > max_len_card:
                max_len_card = int(k)
    print("#{} {} {}".format(i+1, max_len_card, max_len))
