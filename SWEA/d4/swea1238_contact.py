'''
1238. [S/W 문제해결 기본] 10일차 - Contact
'''

import sys
sys.stdin = open("SWEA/inputs/1238_in.txt", "r")
from pprint import pprint

def bfs(g, n, start):
    queue = []
    visited = [0] * (n+1)
    queue.append(start)
    visited[start] = 1

    while queue:
        n_queue = len(queue)
        for _ in range(n_queue):
            dq = queue.pop(0)
            if not visited[dq]:
                visited[dq] = 1
            for next_ in g[dq]:
                if not visited[next_] and next_ not in queue:
                    queue.append(next_)
        flag = True
        for next_ in queue:
            if flag == False:
                break
            if g[next_]:
                for k in g[next_]:
                    if not visited[k]:
                        flag = False
                        break
            
        if flag:
            return max(queue)

def init(nums):
    g = {}
    for i in range(1, len(nums)+1):
        g[i] = []
    for j in range(0, len(nums), 2):
        g[nums[j]].append(nums[j+1])
    
    return g               

t = 10
ans = ""

for tc in range(1, t+1):
    n, start = map(int, input().split())
    nums = list(map(int, input().split()))
    g = init(nums)

    res = bfs(g, n, start)

    ans += "#{} {}\n".format(tc, res)

print(ans)