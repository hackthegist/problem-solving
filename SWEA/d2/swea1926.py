'''
1926. 간단한 369게임
'''

import sys
sys.stdin = open("SWEA/inputs/1926_in.txt", "r")

t = int(input())
claps = ""
br = "369"

for i in range(1, t+1):
    brs = 0
    str_i = str(i)
    for j in str_i:
        if j in br:
            brs += 1
    if brs == 1:
        claps += "- "
    elif brs == 2:
        claps += "-- "
    else:
        claps += str_i + " "


print(claps)
