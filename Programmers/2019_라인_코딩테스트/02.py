


# num = [1, 0, 2]
# num = sorted(num)
# n = len(num)
# idx = 5

# def perm(k):
#     if k == n:
#         print(num)
#     else:
#         for i in range(k, n):
#             num[k], num[i] = num [i], num[k]
#             perm(k+1)
#             num[k], num[i] = num [i], num[k]

# print(perm(0))

# import itertools

# pool = ['A', 'B', 'C']
# print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
# print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기

import itertools

# num = input().strip().split(' ')
num = ['1','0','2']
# idx_t = int(input())
idx_t = 5
print(list(map(''.join, itertools.permutations(num))))

print(sorted(list(map(''.join, itertools.permutations(num)))))