'''
4012. [모의 SW 역량테스트] 요리사
'''

import sys
sys.stdin = open("SWEA/inputs/4012_in.txt", "r")

from itertools import combinations

def get_synergies(lst):
    res = 0
    for i in range(len(lst)-1):
        for j in range(i, len(lst)):
            res += nums[lst[i]][lst[j]] + nums[lst[j]][lst[i]]
    return res

ans = ""

for tc in range(1, int(input())+1):
    n = int(input())
    nums = [list(map(int, input().split())) for _ in range(n)]
    mn = 100000
    
    halves = list(combinations(range(n), n//2))

    set_allnum = set(range(n))
    for half in halves[:len(halves)//2]:
        other = tuple(set_allnum- set(half))
        
        a_syns = get_synergies(half)
        b_syns = get_synergies(other)
        mn = abs(a_syns - b_syns) if mn > abs(a_syns - b_syns) else mn
    res = mn
  
    ans += "#{} {}\n".format(tc, res)

print(ans)