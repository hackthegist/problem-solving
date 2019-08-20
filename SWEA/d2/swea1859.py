'''
1859. 백만 장자 프로젝트
'''
import sys
sys.stdin = open("SWEA/inputs/1859_in.txt", "r")

# 1
# t = int(input())
# answer = ""
# for i in range(t):
#     n = int(input())
#     price = list(map(int, input().split()))
#     result = 0

#     while len(price) > 0:
#         mx = max(price)
#         mx_i = price.index(mx)

#         if mx_i == 0:
#             del price[0]
#             continue

#         for num in price[:mx_i+1]:
#             result += mx - num
#         price = price[mx_i+1:]

#     answer += "#{} {}\n".format(i+1, result)

# print(answer)
# print("#{} {}".format(i+1, result))

# 2 뒤에서부터 탐색

t = int(input())
answer = ""
for i in range(t):
    n = int(input())
    price = list(map(int, input().split()))
    result = 0
    mx = price[-1]
    # print(len(test_case))
    for j in range(len(price)-1, -1, -1):
        if mx <= price[j]:
            mx = price[j]
        else:
            result += mx-price[j]
    answer += "#{} {}\n".format(i+1, result)
print(answer)
