'''
1244. [S/W 문제해결 응용] 2일차 - 최대 상금
'''

import sys
sys.stdin = open("SWEA/inputs/1244_in.txt", "r")

def get_all_cases(str_num):
    n = len(str_num)
    arr = [int(i) for i in str_num]
    tmp = set()

    for j in range(1, n):
        for k in range(j, n):
            arrd = arr[:]
            arrd[j-1], arrd[k] = arrd[k], arrd[j-1]
            tmp.add(''.join(map(str, arrd)))
    return list(tmp)

ans = ""

for tc in range(1, int(input())+1):
    num, chng = input().split()
    chng = int(chng)
    tb = {}
    mx = 0
    
    cases = get_all_cases(num)
    tb[num] = list(set(cases))

    if chng > 1:
        for _ in range(chng-1):
            n_cases = set()
            for case in cases:
                if case in tb.keys():
                    n_cases.update(tb[case])
                else:
                    new = get_all_cases(case)
                    tb[case] = new
                    n_cases.update(new)
            cases = list(n_cases)
        
    res = max(map(int, cases))
    ans += "#{} {}\n".format(tc, res)

print(ans)