'''
1242. [S/W 문제해결 응용] 1일차 - 암호코드 스캔
'''

import sys
sys.stdin = open("SWEA/inputs/1242_in.txt", "r")

def get_codes(codes,m):
    code_list = []
    zero_cnt = m

    for code in codes:
        if code.count('0') == zero_cnt:
            continue
        else:
            # processing = False
            # for i in range(m):
            #     if not processing and code[i] != '0':
            #         first = i
            #         processing = True
            #     if processing and code[i] == '0':
            #         if not (i - first) % 14 == 0:
            #             continue
                    # if i == m-1 or code[i+1] == '0':
                    # last = i
                    # code_list.append(code[first:last])
                    # processing = False
            zero_cnt = code.count('0')

    return code_list

# def is_valid(code):
#     result = 0
#     sum_ = 0

#     patterns = {
#         '0001101': 0,
#         '0011001': 1,
#         '0010011': 2,
#         '0111101': 3,
#         '0100011': 4,
#         '0110001': 5,
#         '0101111': 6,
#         '0111011': 7,
#         '0110111': 8,
#         '0001011': 9
#     }

#     bin_code = '' 
#     for i in range(0, len(code), 2):
#         bin_code += bin(int(code[i:i+1], 16))[:2]
#     r = len(code) % 56
#     nums = '0' * r + nums

    

    for i in range(8):   
        n = patterns[nums[:7]]
        nums = nums[7:]
        sum_ += n

        if i == 7:
            result += n
        elif i % 2 == 0:
            result += n * 3
        else:
            result += n
    
    result = sum_ if result % 10 == 0 else 0

    return result

t = int(input())
ans = ""

for i in range(1, t+1):
    n, m = map(int, input().split())
    codes = [input() for _ in range(n)]
    code_list = get_codes(codes, m)
    print(code_list)

    # ans += "#{} {}\n".format(i, result)

print(ans)