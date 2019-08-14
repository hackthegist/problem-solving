'''
1859. 백만 장자 프로젝트
'''
import sys
sys.stdin = open("../inputs/1859_in.txt", "r")


def get_max_idx(arr):
    m_i = mx = 0
    for i, v in enumerate(arr):
        m_i = i if mx < v else m_i
    return m_i


def get_diff(arr, m_i):
    s = 0
    for v in arr:
        s += arr[m_i] - v
    return s


def get_margin(arr):
    m_i = get_max_idx(arr)
    if m_i == 0:
        return 0
    return get_diff(arr[:m_i+1], m_i)


t = int(input())
for i in range(t):
    n = int(input())
    price = list(map(int, input().split()))
    result = 0

    while len(arr) > 0:
        result += get_margin(price)
        price = price[get_max_idx(price)+1:]

    print("#{} {}".format(i+1, result))
