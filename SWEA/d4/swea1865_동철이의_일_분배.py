'''
1865. 동철이의 일 분배
'''

import sys
sys.stdin = open("SWEA/inputs/1865_in.txt", "r")

t = int(input())
ans = ""

def permutate(k, li, visited):
    base = li[:]
    visited = visited[:]
    global res
    
    print(li)
    if k == n:
        return

    # if k > 0:
    #     for j in range(k):
    #         tmp *= works[j][li[j]]/100
    #         if tmp < res:
    #             return
    #     res = tmp if res < tmp else res
    i = 0
    while sum(visited) < n:
        if not visited[i]:
            base.append(i)
            visited[i] = 1
            permutate(k+1, base, visited)
            if k < n-1:
                visited[i] = 0
            base = li[:]
        i += 1
        i = i % n
        

# def permutate(k):
#     global res
#     tmp = 1

#     for j in range(n):
#         tmp *= works[j][perm_base[j]]/100
#         if tmp < res:
#             return
#     res = tmp if res < tmp else res

#     if k == n:
#         return

    
#     print(k, perm_base, res, '>', tmp)
#     for i in range(k, n):
#         perm_base[k], perm_base[i] = perm_base[i], perm_base[k]
#         permutate(k+1)
#         perm_base[k], perm_base[i] = perm_base[i], perm_base[k]


for i in range(1, t+1):
    n = int(input())
    works = [list(map(int, input().split())) for _ in range(n)]
    perm_base = list(range(n))
    res = 0
    
    # d = [0] * (n+1)
    # if n == 1:
    #     res = works[0]
    # else:
    #     res = 0
    #     for k in range(n):
    #         for y in cp:
    #             temp = works[0][k]*y
    #             res = temp if temp > res else res

    #     d[2] = res
    #     # d[2] = max([x*y for x in works[0] for y in works[1].pop(x))
    #     if n > 2:
    #         for j in range(3, n+1):
    #             d[j] = d[j-1] * max(works[j-1])
            
    #     res = d[n] * (100 ** -(n))
    permutate(0, [], [0]*(n))


    res = round(float(res * 100), 6)
    ans += "#{} {:.6f}\n".format(i, res)

print(ans)