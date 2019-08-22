'''
1267. [S/W 문제해결 응용] 10일차 - 작업순서
'''

import sys
sys.stdin = open("SWEA/inputs/1267_in.txt", "r")

# 1
# def dfs(node, v):
#     visited[node] += 1

#     for i in range(1, v+1):
#         if works_t[node][i] and not visited[i]:
#             dfs(i, v)
#     print(node, end=" ")

#     return


# for i in range(1, 11):
#     v, e = map(int, input().split())
#     nums = list(map(int, input().split()))
#     works_t = [[0] * (v+1) for _ in range(v+1)]

#     for j in range(0, len(nums), 2):
#         works_t[nums[j+1]][nums[j]] += 1

#     visited = [0] * (v+1)
#     print("#{}".format(i), end=" ")

#     for k in range(1, len(visited)):
#         if not visited[k]:
#             dfs(k, v)

#     print()
# works = list(map(int, input().split()))

# ans += "#{} {}\n".format(i, result)

def my_dfs(node, v):
    visited[node] += 1

    while 0 in visited[1:]:
        for i in range(1, (v+1)):
            if works_t[node][i] and not visited[i]:
                stack.append(node)
                node = i
                visited[node] += 1
                print(node, end=" ")
                break
        else:
            if stack:
                node = stack.pop()
            else:
                return


for i in range(1, 11):
    v, e = map(int, input().split())
    nums = list(map(int, input().split()))
    works_t = [[0] * (v+1) for _ in range(v+1)]

    for j in range(0, len(nums), 2):
        works_t[nums[j+1]][nums[j]] += 1

    print("#{}".format(i), end=" ")
    visited = [0] * (v+1)
    stack = []

    for k in range(1, len(visited)):
        if visited[k] == 0:
            my_dfs(k, v)

    print()
