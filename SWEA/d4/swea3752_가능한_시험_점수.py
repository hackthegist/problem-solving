'''
3752. 가능한 시험 점수
'''

import sys
sys.stdin = open("SWEA/inputs/3752_in.txt", "r")

t = int(input())
ans = ""

for tc in range(1, t+1):
    n = int(input())
    scores = [*map(int, input().split())]
    summed = set()
   
    for score in scores:
        if summed:
            summed.update({score + x for x in summed})
        summed.add(score)
        
    res = len(summed) + 1

    ans += "#{} {}\n".format(tc, res)

print(ans)
