'''
5521. 상원이의 생일파티
'''

import sys
sys.stdin = open("SWEA/inputs/5521_in.txt", "r")

ans = ""

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    friends = {k: [] for k in range(n+1)}
    for a, b in [map(int, input().split()) for _ in range(m)]:
        friends[a].append(b)
        friends[b].append(a)

    invited = set(friends[1])
    tmp = set()
    for f in invited:
        tmp.update(friends[f])
    invited.update(tmp)
    
    if 1 in invited:
        res = len(invited) - 1
    else:
        res = len(invited)

    
    ans += "#{} {}\n".format(tc, res)

print(ans)