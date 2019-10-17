'''
5247. [파이썬 S/W 문제해결 구현] 6일차 - 연산
'''

import sys
sys.stdin = open("SWEA/inputs/5247_in.txt", "r")

from collections import deque
ans = ""

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    
    res = 0
    calculated = set()
    
    q = deque()
    q.append(n)
    calculated.add(n)
    while q:
        res += 1
        len_q = len(q)
        for _ in range(len_q):
            dq = q.popleft()
           
            if 0 < dq+1 <= 1000000 and dq+1 not in calculated:
                if dq+1 == m:
                    q = []
                    break
                calculated.add(dq+1)
                q.append(dq+1)
            if 0 < dq-1 <= 1000000 and dq-1 not in calculated:
                if dq-1 == m:
                    q = []
                    break
                calculated.add(dq-1)
                q.append(dq-1)
            if 0 < dq*2 <= 1000000 and dq*2 not in calculated:
                if dq*2 == m:
                    q = []
                    break
                calculated.add(dq*2)
                q.append(dq*2)
            if 0 < dq-10 <= 1000000 and dq-10 not in calculated:
                if dq-10 == m:
                    q = []
                    break
                calculated.add(dq-10)
                q.append(dq-10)
    
    ans += "#{} {}\n".format(tc, res)

print(ans)