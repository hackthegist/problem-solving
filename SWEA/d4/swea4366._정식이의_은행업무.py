'''
4366. 정식이의 은행업무
'''

import sys
sys.stdin = open("SWEA/inputs/4366_in.txt", "r")

def get_from_two(two):
    res = []
    for i in range(len(two)):
        base = two[:]
        if two[i] == '0':
            base[i] = '1'
        else:
            base[i] = '0'
        res.append(''.join(base))
    return res

def get_from_three(three):
    res = []
    rests = '012'
    for i in range(len(three)):
        for j in rests:
            base = three[:]
            if base[i] != j:
                base[i] = j
                res.append((''.join(base)))
    return res

t = int(input())
ans = ""

for i in range(1, t+1):
    two = list(input())
    three = list(input())

    res2 = get_from_two(two)
    res3 = get_from_three(three)

    for x in res2:
        for y in res3:
            if int(x, 2) == int(y, 3):
                res = int(y, 3)
                break



    ans += "#{} {}\n".format(i, res)

print(ans)