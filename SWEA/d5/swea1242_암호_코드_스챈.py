'''
1242. [S/W 문제해결 응용] 1일차 - 암호코드 스캔
'''

import sys
sys.stdin = open("SWEA/inputs/1242_in.txt", "r")

def decode(code):
    dec = ''
    code = code.rstrip('0')
    for i in range(len(code)-2, -1, -2):
        sixteen = code[i:i+2]
        bin_c = bin(int(sixteen, 16))[2:]
        dec = ('0'*(8-len(bin_c))) + bin_c + dec
    dec = '000' + dec.lstrip('0') + '0'

    return dec 

def get_codes(codes):
    code_list = []

    for i in range(1, len(codes)):
        if codes[i] == codes[i-1]:
            continue
        else:
            codes_cp = codes[i][:]
            for j in range(len(codes[i])):
                if codes[i][j] != 0 and codes[i][j] == codes[i-1][j]:
                    codes_cp[j] = '0'
            code_list.append(decode(''.join(codes_cp)))
            # code_list.append(decode2(codes[i]))

    return code_list

def is_valid(bin_code):
    res = sum_ = result = elem = 0
    patterns = {
        (2,1,1): 0,
        (2,2,1): 1,
        (1,2,2): 2,
        (4,1,1): 3,
        (1,3,2): 4,
        (2,3,1): 5,
        (1,1,4): 6,
        (3,1,2): 7,
        (2,1,3): 8,
        (1,1,2): 9
    }

    bin_code = bin_code.lstrip('0') 
    pattern = ''
    cnt = [0] * 3

    for ch in bin_code:
        if ch == '1':
            if cnt[1] == 0:
                cnt[0] += 1
            else:
                cnt[2] += 1
        if ch == '0':
            if cnt[0] > 0 and cnt[2] == 0:
                cnt[1] += 1
            else:
                if cnt[0] > 0:
                    if not tuple(cnt) in patterns.keys():
                        while tuple(cnt) not in patterns.keys():
                            det = min(cnt)
                            cnt = list(map(lambda x: x//det, cnt))
                    n = patterns[tuple(cnt)]
                    elem += 1
                    cnt = [0] * 3
                    # print('#{} {}'.format(elem, n), end=" ")

                    sum_ += n
                    if elem == 8:
                        result += n
                    elif elem % 2 == 1:
                        result += n * 3
                    else:
                        result += n

                    if elem == 8:
                        res += sum_ if result % 10 == 0 else 0
                        sum_ = result = elem = 0 
                else: 
                    continue

    return res

t = int(input())
ans = ""

for i in range(1, t+1):
    n, m = map(int, input().split())
    codes = [list(input()) for _ in range(n)]
    code_list = get_codes(codes)
    code_list = set(code_list)
    # print(code_list)
    res = sum([is_valid(code) for code in code_list])
    ans += "#{} {}\n".format(i, res)

print(ans)