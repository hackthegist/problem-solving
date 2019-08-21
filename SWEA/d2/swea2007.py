'''
2007. 패턴 마디의 길이
'''

import sys
sys.stdin = open("SWEA/inputs/2007_in.txt", "r")

t = int(input())
answer = ""


for i in range(1, t+1):
    found = False
    words = input()
    for j in range(1, len(words)):
        if words[0] == words[j]:
            for k in range(j):
                if words[k] != words[k+j]:
                    break
            else:
                found = True
        if found:
            break
    answer += "#{} {}\n".format(i, j)


print(answer)
